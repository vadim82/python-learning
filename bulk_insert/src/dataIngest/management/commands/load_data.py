from contextlib import closing
import csv
import datetime
from io import StringIO
import json
from sqlite3 import Cursor
import time
from typing import Any, List
from django.core.management.base import BaseCommand, CommandParser
from django.db import connection, transaction

from dataIngest.models import CassiniData
class Command(BaseCommand):
    

    help = 'Bulk upserts data into database'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('--file_path', '-f', type=str, required=True)

    def option_1(self, data: List[Any]):
        start = time.time()
        items = [CassiniData(**x) for x in data["items"]]

        CassiniData.objects.bulk_create(items, batch_size=500)
        end = time.time()
        print ("Time elapsed:", end - start)   

    def option_2(self, data: List[Any]):
        stream = StringIO()
        writer = csv.writer(stream, delimiter='\t')

        start = time.time()

        for i in range(0, len(data["items"])):
            writer.writerow( x.replace('\\', '\\\\') for x in list(data["items"][i].values()) )
    
        stream.seek(0)

        with closing(connection.cursor()) as cursor:
            cursor.copy_from(
                file=stream,
                table="cassinni_data",
                sep='\t',
                columns=list(data["items"][0].keys())
            )
        end = time.time()
        print ("Time elapsed:", end - start)     

    def option_3(self, data: List[Any]):
        stream = StringIO()
        writer = csv.writer(stream, delimiter='\t')

        start = time.time()

        for i in range(0, len(data["items"])):
            writer.writerow( x.replace('\\', '\\\\') for x in list(data["items"][i].values()) )
    
        stream.seek(0)

        with closing(connection.cursor()) as cursor:
            cursor: Cursor
            # with transaction.atomic():
            
            table_name = f"cassini_data_{time.time_ns()}"

            cursor.execute(f"""
                create unlogged table {table_name} as table cassinni_data with no data;
                alter table {table_name} drop column id;
            """)

            cursor.execute(f""" 
                create unique index ix_{table_name}_identifier on {table_name}(identifier);
            """)

            cursor.copy_from(
                file=stream,
                table=table_name,
                sep='\t',
                columns=list(data["items"][0].keys()),
            )
            end = time.time()
            print ("Staging Data: Time elapsed:", end - start)

            columns = [f.name for f in CassiniData._meta.fields if not f.primary_key]
            statements = ", ".join(f"{c} = excluded.{c}" for c in columns)
            print(statements)
            cursor.execute(f"""
                INSERT INTO cassinni_data({','.join(columns)})
                SELECT * from {table_name}
                ON CONFLICT (identifier) do
                UPDATE SET {statements};
            """)

            cursor.execute(f"drop table {table_name}")

        end = time.time()
        print ("Total Time elapsed:", end - start)

    def handle(self, *args, **options):
        with open(options["file_path"], "r") as f:
            data = json.load(f)
            self.option_3(data)
    