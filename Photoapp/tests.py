from django.test import TestCase
from .models import Photo,Category,Location
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

class PhotoTestClass(TestCase):

    def setUp(self):

        self.new_category = Category(category='main')
        self.new_category.save()

        self.new_location = Location(location='eldoret')
        self.new_location.save()

        self.new_photo = Photo(image='cal.jpg',title='Talia',description='Breath taking view',category=self.new_category,location=self.new_location)
        self.new_photo.save()


    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Photo.objects.all().delete()


    def test_search_by_location(self):
        search_by_location = Photo.objects.filter(location__location=self)

        return search_by_location

    def test_search_by_category(self):
        search_by_category = Photo.objects.filter(category__category=self)

        return search_by_category

    def test_update_photo(self):

        self.updated_category = Category(category='sub')
        self.updated_category.save()

        self.updated_location = Location(location='Nairobi')
        self.updated_location.save()

        self.updated_photo = Photo.objects.filter(image=self.id).update(image='Varsia.jpg',title='Vars',description='Most viewed belief',category=self.updated_category,location=self.updated_location)


    def test_get_by_id(self):
        get_by_id = Photo.objects.filter(pic=self.id)

        return get_by_id




    

