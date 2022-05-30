from email.mime import image
from django.db import models
from cloudinary.models import CloudinaryField


class Location(models.Model):
    location = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        Location.objects.filter(location=self).delete()

    def update_location(self):
        Location.objects.filter(location=self).update(location=self.location)

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def delete_category(self):
        Category.objects.filter(category=self).delete()

    def update_category(self):
        Category.objects.filter(category=self).update(category=self.category)




class Photo(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=60)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    description = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True)

    @classmethod
    def photos(cls):
        photos = cls.objects.all()

        return photos

    @classmethod
    def get_by_id(cls, id):
        photo = cls.objects.filter(id=id)

        return photo

    @classmethod
    def search_by_location(cls, search_term):
        photos = cls.objects.filter(location__location=search_term)

        return photos


    @classmethod
    def search_by_category(cls, search_term):

        photos = cls.objects.filter(category__category=search_term)

        return photos

    def update_photo(self):
        updated_photo = Photo.objects.filter(pic=self.id).update(image=self.image,title=self.title,description=self.description,category=self.category,location=self.location)
        
        return updated_photo


    def save_image(self):
        self.save()

    def delete_image(self):
        Photo.objects.filter(id=self).delete()









        