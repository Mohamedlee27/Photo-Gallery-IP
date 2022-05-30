from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Photo


def photos(request):
    photos = Photo.photos()

    return render(request,'index.html',{"photos":photos})