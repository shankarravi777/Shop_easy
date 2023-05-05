import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from myapp.models import *

class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        Product.objects.all().delete()
        print("tables dropped successfully")

        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/myapp/data/data.csv',encoding='cp1252', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)

                price=0.0
                x=float(row[22])
                print(x)
                if(x):
                    price=x

                product = Product.objects.create(
                    name = row[3],
                    price = price,
                    images = row[14]
                )
                product.save()
