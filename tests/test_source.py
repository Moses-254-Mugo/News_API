import unittest
from app.models import Source 

class ArticleTest(unittest. TestCase):
    '''
    Test class to test the behaviour of the source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source()

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
