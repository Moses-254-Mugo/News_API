import unittest
from models import Article
Article = article.Article
 
class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('abc','new weapon in market','new weapon released','url',2010-8-8,'read more')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))


if __name__ == '__main__':
    unittest.main()