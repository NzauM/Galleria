from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Picture


# Create your views here.
def pics(request):
    pics = Picture.all_pics()
    return render(request,'all_pics.html',{"pics":pics})

def single_pic(request,pic_id):
    pic = Picture.objects.get(id = pic_id)
    return render(request,"single_pic.html", {'pic':pic})

