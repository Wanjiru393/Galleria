from email.mime import image
from unicodedata import category
from django import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('explore', views.explore, name='explore'),
    path('search', views.search, name='search'),
    path('category/<int:category_id>/', views.imageCategory, name='category'),
    path('location/<int:location_id>/', views.imageLocation, name='location'),
    path('image/<int:image_id>/', views.displayImage, name='image'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)