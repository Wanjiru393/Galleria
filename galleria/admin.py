from django.contrib import admin
from .models import *
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal= ('tags',)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image, ImageAdmin)
admin.site.register(Tags)