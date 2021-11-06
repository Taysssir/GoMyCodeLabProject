from django.test import TestCase
from . models import BlogPost
from account.models import Account


# Create your tests here.
class ModelTesting(TestCase):

    def setUp(self):
        self.account = Account.objects.create(username='Tayssir',email='taysir.boubaker2082@gmail.com' )
        self.blog = BlogPost.objects.create(title='django', body='Test Blog', author=self.account, slug='django')

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, BlogPost))
        self.assertEqual(str(d), 'django')
	