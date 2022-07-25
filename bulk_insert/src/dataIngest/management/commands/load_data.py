from contextlib import closing
import csv
import datetime
from io import StringIO
import json
from sqlite3 import Cursor
import time
import uuid
from django.core.management.base import BaseCommand, CommandParser
from django.db import connection, transaction
from psycopg2.extensions import cursor

from dataIngest.models import CassiniData
class Command(BaseCommand):
    

    help = 'Bulk upserts data into database'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('--file_path', '-f', type=str, required=True)

    def handle(self, *args, **options):
        with open(options["file_path"], "r") as f:
            data = json.load(f)
            #print(data["items"][0])
            # for row in data["items"]:
            #     model = CassiniData(
            #         **row
            #     )

            # start = time.time()
            # items = [CassiniData(**x) for x in data["items"]]
            # CassiniData.objects.bulk_create(items, batch_size=500)
            # end = time.time()
            # print ("Time elapsed:", end - start)

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


            # with closing(connection.cursor()) as cursor:
            #     cursor: Cursor
            #     # with transaction.atomic():
                
            #     table_name = f"cassini_data_{time.time_ns()}"

            #     cursor.execute(f"""
            #         create table {table_name} (
            #             start_time_utc    character varying(200),
            #             duration           character varying(250),
            #             date               character varying(50),
            #             team               character varying(25),
            #             spass_type         character varying(100),
            #             target             character varying(25),
            #             request_name       character varying(50),
            #             library_definition character varying(250),
            #             title              character varying(250),
            #             description        text,
            #             identifier         uuid not null
            #         );
            #     """)

            #     cursor.execute(f""" 
            #         create unique index ix_{table_name}_identifier on {table_name}(identifier);
            #     """)

            #     cursor.copy_from(
            #         file=stream,
            #         table=table_name,
            #         sep='\t',
            #         columns=list(data["items"][0].keys()),
            #     )
            #     end = time.time()
            #     print ("Time elapsed:", end - start)

            #     cursor.execute(f"""
            #         INSERT INTO cassinni_data(start_time_utc, duration,date,team,spass_type,target,request_name,library_definition,title,description,identifier )
            #         SELECT * from {table_name}
            #         ON CONFLICT (identifier) do
            #         UPDATE SET title = 'Updated';
            #     """)

            #     cursor.execute(f"drop table {table_name}")

            # end = time.time()
            # print ("Time elapsed:", end - start)