import unittest
from models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        
        self.new_article = Article('The New York Times','BROOKS BARNES','Amazon Resets Its Film Operation After Rough Year at Box Office','The tech giant put “too much focus” on art-house fare, the head of Amazon Studios said. The tech giant will now focus more on films for a broader audience, including “sexy date-night movies.',' "https://www.nytimes.com/2019/02/18/business/media/amazon-movies-jennifer-salke.html','https://static01.nyt.com/images/2019/02/19/business/19AMAZONFILM-01/19AMAZONFILM-01-facebookJumbo.jpg','2019-02-19T00:10:57Z','Its really about creating that right marketing campaign, right distribution plan for each movie, allowing us to break through the cultural noise and really resonating with customers, said Matt Newman, one of three executives Ms. Salke has named as film co-chi… [+3119 chars]')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()