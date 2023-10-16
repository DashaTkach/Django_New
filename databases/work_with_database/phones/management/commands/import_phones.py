import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for line in phones:
                phone = Phone(id=line['id'], name=line['name'], price=line['price'], image=line['image'],
                              release_date=line['release_date'], lte_exists=line['lte_exists'])
                phone.save()
