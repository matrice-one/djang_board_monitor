import json
from django.core.management.base import BaseCommand
from visual_board.models import BoardMember, Company
from tqdm import tqdm

class Command(BaseCommand):
    help = 'Loads data from a JSON file and creates objects in the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The path to the JSON file')

    def handle(self, *args, **options):
        # Open the JSON file and load the data
        with open(options['json_file'], 'r') as f:
            data = json.load(f)

        companies = {}

        for i, item in enumerate(tqdm(data, desc='Processing board member {i}')):
            board_member_name = item['Name and Surname']
            board_member_signature_mode = item['Signature mode']
            board_member_status = item['Status']
            board_member = BoardMember(name_and_surname=board_member_name, signature_mode=board_member_signature_mode, status=board_member_status)
            board_member.save()

            company_name = item['Company']
            if company_name not in companies:
                company = Company(name=company_name)
                company.save()  # Save the company to the database to generate an id
                companies[company_name] = company

            company_name = item['Company']
            board_member_name = item['Name and Surname']
            company = companies[company_name]
            board_member = BoardMember.objects.filter(name_and_surname=board_member_name).last()
            company.board_members.add(board_member)

