from django.db import models
from django_resized import ResizedImageField
from django.utils import timezone
from django.db import models


# Category model
class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

    def saveCategory(self):
        self.save()


# Location model
class Location(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    def saveLocation(self):
        self.save()


# Tags model
class Tags(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
   

# Images Model
class Image(models.Model):
    # image = models.ImageField(upload_to = 'articles/', blank=True)
    image = ResizedImageField(size=[2878, 1618], crop=['middle', 'center'], upload_to='art/', blank=True)
    imageName = models.CharField(max_length=60)
    description = models.TextField()
    uploadDate = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags= models.ManyToManyField(Tags)
    
    def __str__(self):
        return self.imageName

    def saveImage(self):
        return self.save()

    def deleteImage(self):
        self.delete()

    def updateImage(self):
        self.update()

    
    @classmethod
    def getImages(cls):
        allImages = cls.objects.all()
        return allImages
    @classmethod
    def getImagebyId(cls,id):
        getImage = cls.objects.filter(image_id=id)
        return getImage

    @classmethod
    def filterByLocation(cls,id):
        imageLocation = cls.objects.filter(location_id=id)
        return imageLocation

    @classmethod
    def filterByCategory(cls,id):
        imageCategory = cls.objects.filter(category_id=id)
        return imageCategory
    
    @classmethod
    def searchImage(cls,search_term):
        searchedImage = cls.objects.filter(category__name__icontains=search_term)
        return searchedImage

     