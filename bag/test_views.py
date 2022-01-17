from django.test import TestCase
from django.shortcuts import reverse


class TestBagViews(TestCase):

    def test_bag_page_url_exists(self):
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
