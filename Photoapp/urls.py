from django.urls import re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
     url('admin/', admin.site.urls,name='admin'),
     url('',views.photos,name='photos'),
     url('category/',views.category_results,name='category'),
     url('location/',views.location_results,name='location'),
     url('photo/(\d+)/',views.photo,name='photo')

]