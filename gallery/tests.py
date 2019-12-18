from django.test import TestCase
from .models import Author,Category,Location,Picture


# Create your tests here.
class AuthorTest(TestCase):
    def setUp(self):
        self.TestAuthor = Author(first_name = 'Test', last_name = 'Author',email = 'tester@gmail.com' ,phone_number = '0711111446')

    def test_instance(self):
        '''
        To test correct instantiation
        '''
        self.assertTrue(isinstance(self.TestAuthor,Author))
        

        

    def test_author_save(self):
        '''
        Test class to confirm that authors are saved succesfully
        '''
        self.TestAuthor.save_author()
        authors = Author.objects.all()
        self.assertTrue(len(authors) > 0)

class PictureTest(TestCase):
    def setUp(self):
        self.TestPicture = Picture(image = 'images.url',name = 'Image', description = 'This is an image',location = 'Nairobi',Category = 'Flowers',author ='Mercy')

    def test_instance(self):
        '''
        Test instantiation
        '''
        self.assertTrue(isinstance(self.TestPicture))


    def test_save_picture(self):
        '''
        Function to see that a picture is saved to the db
        '''
        self.TestPicture.save_pic():
        pictures = Picture.objects.all()
        self.assertTrue(len(pictures) > 0)

    def test_delete_picture(self):
        '''
        Tests deletion of picture objects
        '''
        self.TestPicture.save_pic()
        Pic = get_one_pic(image)
        pics = all_pics()
        pics.delete()
        self.assertTrue(len(pics) == 0 )

    def test_get_one_pic(self):
        '''
        To test if we can get an image using the image id
        '''
        self.TestPicture.save_pic()
        pic = get_one_pic(image)
        pics = Picture.objects.all()
        self.assertTrue(len(pics) > 0)

    def test_all_pics(self):
        '''
        To test getting all pics 
        '''
        self.TestPicture.save_pic()
        pics = all_pics()
        pictures = Picture.objects.all()
        self.assertTrue(len(pics) == len(pictures))

class CategoryTest(TestCase):
    def setUp(self):
        Test_category = Category(name = 'Technology')

    def test_instance(self):
        '''
        Test instantiation of the category
        '''
        self.assertTrue(isinstance(self.Test_category))

    def test_save_category(self):
        self.Test_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_get_categories(self):
        self.Test_category.save_category()
        categories = Category.get_categories()
        cats = Category.objects.all()
        self.assertTrue(len(categories) == len(cats))


class LocationTest(TestCase):
    def setUp(self):
        Test_Location = Location(name = 'Nairobi')

    def test_instance(self):
        '''
        Test instantiation of the location class
        '''
        self.assertTrue(isinstance(self,Test_Location))

    def test_save_location(self):
        self.Test_Location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_get_locations(self):
        self.Test_Location.save_location()
        Locations = Location.get_location()
        locations_all = Location.objects.all()
        self.assertTrue(len(Locations) == len(locations_all))
