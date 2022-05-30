from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Photo


def photos(request):
    photos = Photo.photos()

    return render(request,'index.html',{"photos":photos})

def location_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_location(search_term)

        message = f"{search_term}"

        return render(request,'results.html',{"message":message,"photos":searched_photos})

    else:
        message = "You have not searched a photo yet"

        return render(request,'results.html',{"message":message})
