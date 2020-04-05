#!/usr/bin/env python3

# initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'arcticapi.settings'
import django
django.setup()

# regular imports
from api.models import Category, Product
import json


# main script
def main():

    Product.objects.all().delete()
    Category.objects.all().delete()
    

    #for cat in Category.objects.all():
    #    print(cat.id, cat.title)
    c2 = Category()
    c2.title = "Office"
    c2.save()
    c3 = Category()
    c3.title = "Clothes"
    c3.save()
    c4 = Category()
    c4.title = "Food"
    c4.save()
    c5 = Category()
    c5.title = "Household"
    c5.save()
    c6 = Category()
    c6.title = "Other"
    c6.save()
    c7 = Category()
    c7.title = "Ducks"
    c7.save()

    for cat in Category.objects.all():
        print(cat.id, cat.title)

    # read JSON file
    with open('products.json') as json_file:
        data=json.load(json_file)
    products = data['products']
    # loop through JSON
        # create products
    for prod in products:
        dbprod = Product()
        dbprod.name = prod['name']
        dbprod.category = Category.objects.get(title=prod['category'])
        dbprod.filename = prod['filename']
        dbprod.description = prod['description']
        dbprod.price = prod['price']
        dbprod.save()
    
    

# bootstrap
if __name__ == '__main__':
    main()
