from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Article


# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        # create and save user
        self.test_user = User(username='cephas',password='admin121',email='cephaske254@gmail.co,',first_name='cephas', last_name='too')
        self.test_user.save()
        
        self.user = User.objects.filter(username=self.test_user.username).first()
        
        # create user profile
        self.profile = Profile.save_profile(self.user, 'bio here', '0702149456', 'avatar.png')
        

    def tearDown(self):
        self.user.delete()

    def test_save_user(self):
        self.assertTrue(len(User.objects.all()) >0 )

    def test_save_profile(self):
        self.assertTrue(len(Profile.get_all_profiles()) >0)

    def test_instance(self):
        self.assertTrue(isinstance(self.test_user, User))

    def test_get_profile(self):
        Profile.get_profile(self.user)

    def test_update_profile(self):
        updated_user = Profile.update_profile(self.user,'','0712345678','avatar1.png')
        self.assertEqual(updated_user, self.profile)
        # should not set the field to null if an empty value is passed
        self.assertEqual(updated_user.bio, 'bio here')
        
    def test_search_profiles(self):
        profiles = Profile.search_profile(self.user.username)
        self.assertTrue(len(profiles)>0)

class ArticleTest(TestCase):
    def setUp(self):

        self.test_user = User(username='cephas',password='admin121',email='cephaske254@gmail.co,',first_name='cephas', last_name='too')
        self.test_user.save()
        # get saved_user
        self.user = User.objects.filter(username=self.test_user.username).first()
        # create article
        self.test_article = Article.save_article(self.user,'title','http:localhost','description',True)
        self.article = Article.objects.filter(user=self.test_user.id).first()

    def tearDown(self):
        self.article.delete()
        self.user.delete()

    def test_save_article(self):
        self.assertTrue(len(Article.objects.all()) >0)

    
    def test_get_article(self):
        article = Article.get_article(self.article.id)
        self.assertEqual(article.link, self.test_article.link)
        self.assertEqual(article, self.test_article)

    def test_update_article(self):
        updated_article = Article.update_article(self.article.id, 'titleeee','http:google.com','description', False)
        self.assertIsNotNone(updated_article)
        self.assertNotEqual(str(self.article), str(updated_article))
    
    def test_get_all_articles(self):
        articles = Article.get_all_articles()
        self.assertIsNotNone(articles)
    
    def test_search_articles(self):
        articles = Article.search_articles(self.article.title)
        self.assertIsNotNone(articles)
        

