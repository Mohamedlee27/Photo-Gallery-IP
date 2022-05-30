from django.db import models
import datetime as dt

class Image(models.Model):
    pic = CloudinaryField('image')
    title = models.CharField(max_length=60)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True)
    published = models.DateTimeField(auto_now_add=True)
