from django.test import TestCase
from .models import *
# Create your tests here.


class LocationTestClass(TestCase):
    def setUp(self):
        self.kenya = Location(name='Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.kenya,Location)) 

    def test_save_method(self):
        self.kenya.saveLocation()
        location = Location.objects.all()
        self.assertTrue(len(location)>0)   

class CategoryTestClass(TestCase):
    def setUp(self):
        self.food = Category(name='Food')

    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category)) 

    def test_save_method(self):
        self.food.saveCategory()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)   

# Image Test
class ImageTest(TestCase):
    def setUp(self):
        self.Food = Category(name='Food')
        self.Food.save_category()

        self.new_location = Location(name='Kenya')
        self.new_location.save()

        self.new_tag = Tags(name = 'testing')
        self.new_tag.save()

        self.new_image=Image(image_name='foods',image_description='Chinese Delicacy')
        self.new_image.save_image() 

        self.new_image.Category.add(self.new_category)
        self.new_image.Location.add(self.new_location)
        self.new_image.Tags.add(self.new_tag)

        def tearDown(self):
            Image.objects.all().delete()
            Category.objects.all().delete()
            Location.objects.all().delete()
            Tags.objects.all().delete()

        def test_deleteImage(self):
            
            self.new_image.deleteImage()
            image = Image.objects.all()
            self.assertEqual(len(image),0)

        def test_updateImage(self):
            
            self.new_image.updateImage()
            updatedImage = Image(image_name='Kenyan foods',image_description='Kenyan Delicacy')
            self.new_image.save_image() 


        def test_getImages(self):
            allImages = Image.getImages()
            self.assertTrue(len(allImages)>0)
        
        def test_getImagebyId(self):
            test_id=1
            getImage = Image.objects.filter(test_id)
            self.assertTrue(len(getImage)>0)

        def test_filterByLocation(self):
            testLocationId = 1
            imageLocation = Image.filter(testLocationId)
            self.assertTrue(len(imageLocation)==0)

        def test_filterByCategory(self):
            testCategoryId = 1
            imageCategory = Image.filter(testCategoryId)
            self.assertTrue(len(imageCategory)==0)



