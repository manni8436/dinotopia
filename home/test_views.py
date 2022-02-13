from django.test import TestCase
from django.shortcuts import reverse


class TestHomeViews(TestCase):

    def test_home_page_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_the_home_url_is_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
