from email.mime import image
from django.db import models
import datetime as dt

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
    def search_by_location(cls, location_term):
        photos = cls.objects.filter(location__location=location_term)

        return photos


    @classmethod
    def search_by_category(cls, category_term):

        photos = cls.objects.filter(category__category=category_term)

        return photos

    def update_photo(self):
        updated_photo = Photo.objects.filter(pic=self.id).update(image=self.image,title=self.title,description=self.description,category=self.category,location=self.location)
        
        return updated_photo


    def save_image(self):
        self.save()

    def delete_image(self):
        Photo.objects.filter(id=self).delete()



        