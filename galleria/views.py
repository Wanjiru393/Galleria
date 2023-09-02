from django.shortcuts import render, redirect

from email import message
from django.http import HttpResponse,Http404
from .models import *
# Create your views here.

# View for home page
def home(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render (request, 'home.html',{"categories": categories, "locations": locations})


# view for explore page
def explore(request):
    # images = Image.objects.all()
    images = Image.getImages()
    locations = Location.objects.all()
    categories = Category.objects.all()

    # context = {}
    # context['images'] = images

    return render (request, 'explore.html', {"images": images, "categories": categories, "locations": locations})# view for search page

def imageCategory(request, category_id):
    locations = Location.objects.all()
    categories = Category.objects.all()
    try:
        displaycategories=Image.filterByCategory(category_id)

    except Image.DoesNotExist:
        raise Http404()
    return render(request, 'category.html', {"categories": categories, "locations": locations, "displaycategories":displaycategories})

def imageLocation(request, location_id):
    locations = Location.objects.all()
    categories = Category.objects.all()
    try:
        displaylocations=Image.filterByLocation(location_id)

    except Image.DoesNotExist:
        raise Http404()
    return render(request,'location.html', {"categories": categories, "locations": locations,"displaylocations": displaylocations}) 

def displayImage(request, image_id):
    locations = Location.objects.all()
    categories = Category.objects.all()
    try:
        displayImage=Image.objects.get(id = image_id)

    except Image.DoesNotExist:
        raise Http404()
    return render(request,'image.html', {"categories": categories, "locations": locations,"displayImage": displayImage}) 



def search(request):
    locations = Location.objects.all()
    categories = Category.objects.all()

    if 'searchedImage' in request.GET and request.GET["searchedImage"]:
        search_term = request.GET.get("searchedImage")
        searchedImages = Image.searchImage(search_term)
        message=f"{search_term}"
        return render (request, 'search.html',{"message":message,"searchedImages": searchedImages, "categories": categories, "locations": locations})
    else:
        message = "You haven't searched for any term"
        return render(request, 'explore.html',{"message":message, "categories": categories, "locations": locations})

