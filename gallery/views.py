from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Picture


# Create your views here.
def pics(request):
    pics = Picture.all_pics()
    return render(request,'all_pics.html',{"pics":pics})
