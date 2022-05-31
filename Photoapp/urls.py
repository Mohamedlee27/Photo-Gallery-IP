from django.urls import re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
  
     url(r'^$',views.photos,name='photos'),
     url(r'^category/',views.category_results,name='category'),
     url(r'^location/',views.location_results,name='location'),
     url(r'^photo/(\d+)/',views.photo,name='photo')

]