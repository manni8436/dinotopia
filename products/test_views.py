from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.
class TestProductsViews(TestCase):

    def test_products_page_url_exists(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_the_products_url_is_accessible_by_name(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_products_page_template(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
