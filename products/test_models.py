from django.test import TestCase
from .models import Category, Product


class TestCategoryModels(TestCase):

    def test_category_str(self):
        test_case = Category() # declared test_case as a Category class.
        test_case.name = "testing" # declared test_case.name and changing the property instance (which has been declared as Category in the line above) as testing (which is a string)
        self.assertEqual(str(test_case), "testing") # calling the __str__ function from inside the class.

    def test_category_friendly_name(self):
        test_case = Category()
        test_case.friendly_name = "testing"
        self.assertEqual(test_case.get_friendly_name(), "testing") # this is a more normal way of calling a class function.

class TestProductModels(TestCase):

    def test_product_str(self):
        test_case = Product()
        test_case.name = "testing"
        self.assertEqual(str(test_case), "testing")
