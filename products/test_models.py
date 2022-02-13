from django.test import TestCase
from .models import Category, Product


class TestCategoryModels(TestCase):

    def test_category_str(self):
        """testing category models __str__"""
        test_case = Category()
        test_case.name = "testing"
        self.assertEqual(str(test_case), "testing")

    def test_category_friendly_name(self):
        """testing category models friendly name"""
        test_case = Category()
        test_case.friendly_name = "testing"
        self.assertEqual(test_case.get_friendly_name(), "testing")


class TestProductModels(TestCase):

    def test_product_str(self):
        """testing products models __str__"""
        test_case = Product()
        test_case.name = "testing"
        self.assertEqual(str(test_case), "testing")
