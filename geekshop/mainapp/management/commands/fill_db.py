from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from django.contrib.auth.models import User

import json, os

JSON_PATH = 'mainapp/fixtures'


def load_from_json(file):
    with open(os.path.join(JSON_PATH, file + '.json'), 'r', encoding='utf') as f:
        return json.load(f)


class Command(BaseCommand):
    def handle(self, *args, **options):
        pc = load_from_json('pc')
        ProductCategory.objects.all().delete()
        for el in pc:
            cat = el.get('fields')
            cat['id'] = el.get('pk')
            new_pc = ProductCategory(**cat)
            new_pc.save()

        p = load_from_json('p')
        Product.objects.all().delete()
        for el in p:
            prod = el.get('fields')
            prod['category'] = ProductCategory.objects.get(id=prod.get('category'))
            new_p = Product(**prod)
            new_p.save()
        User.objects.all().delete()
        super_user = User.objects.create_superuser('s', 'a@b.com', '1')
