from django.test import TestCase
from .models import Image,Category,Location
import datetime as dt


class CategoryTestClass(TestCase):

    # set up method
    def setUp(self):
        self.general = Category(category='general')

    # test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.general,Category))

    # test the save method
    def test_save_method(self):
        self.general.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)

    def tearDown(self):
        Category.objects.filter(category='general').delete()

    def test_update_category(self):
        Category.objects.filter(category='general').update(category='health')

