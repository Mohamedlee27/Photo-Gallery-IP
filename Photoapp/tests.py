from django.test import TestCase
from .models import Image,Category,Location
import datetime as dt


class LocationTestClass(TestCase):


    def setUp(self):
        self.eldoret = Location(location='eldoret')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.eldoret,Location))

    
    def test_save_method(self):
        self.eldoret.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_update_location(self):
        Location.objects.filter(location='eldoret').update(location='nairobi')

    def tearDown(self):
        Location.objects.filter(location='eldoret').delete()


class CategoryTestClass(TestCase):

    
    def setUp(self):
        self.main = Category(category='main')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.main,Category))

    
    def test_save_method(self):
        self.main.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)

    def tearDown(self):
        Category.objects.filter(category='main').delete()

    def test_update_category(self):
        Category.objects.filter(category='main').update(category='sub')




    

