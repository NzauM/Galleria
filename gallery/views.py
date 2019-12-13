from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Picture


# Create your views here.
def pics(request):
    pics = Picture.all_pics()
    return render(request,'all_pics.html',{"pics":pics })

def single_pic(request,id):
    try:
        pic = Picture.objects.get(id = id)
    except DoesNotExist:
        raise Http404()
    return render(request,"single_pic.html", {"pic":pic})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get('image')
        searched_pics = Picture.search_by_name(search_term)
        message = f'{search_term}'

        return render(request,'search.html',{"message":message,"image":searched_pics})

    else:
        message = "You have not entered anything to search"
        return render(request,'search.html',{"message":message})
