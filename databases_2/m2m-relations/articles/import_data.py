import json

from django.core.management.base import BaseCommand
from articles.models import Article


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def get_data(self):
        with open('article.json') as file:
            data = json.load(file)

            for article in data:
                element = Article(title=article['fields']['title'], text=article['fields']['text'],
                                  published_at=article['fields']['published_at'], image=article['fields']['image'])
                element.save()
