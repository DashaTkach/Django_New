import csv
from pprint import pprint

with open('phones.csv', 'r') as file:
    phones = list(csv.DictReader(file, delimiter=';'))
    pprint(phones)
