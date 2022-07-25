from django.core.management.base import BaseCommand, CommandError, CommandParser
import csv
import json
import uuid

class Command(BaseCommand):

    help = 'Converts csv file to json file'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('--file_path', '-f', type=str, required=True)
        parser.add_argument('--output_path', '-o', type=str, required=True)

    def handle(self, *args, **options):

        data_dict = {
            "items": []
        }
        with open(options['file_path'], 'r', newline='') as csv_file:

            reader = csv.DictReader(csv_file)
            for row in reader:
                row["identifier"] = str(uuid.uuid4())
                data_dict["items"].append(row)

        with open(options['output_path'], 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(data_dict, indent=4))
