from django.test import TestCase
from mainapp.models import ProductCategory, Product
from django.test.client import Client


class TestMainSmokeTest(TestCase):

    def setUp(self):
        category = ProductCategory.objects.create(name='NewCat')
        Product.objects.create(category=category, name='new_produst', price=100)
        self.client = Client()

    def test_products_pages(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        response = self.client.get('/users/profile/')
        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        pass
