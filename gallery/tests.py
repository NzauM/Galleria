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
        
