from django.test import TestCase, Client
from . models import MyAccountManager,Account
from . forms import *
import pytest


# Create your tests here.
class ModelTesting(TestCase):

    def setUp(self):
        #self.account_manager = MyAccountManager.objects.create(username='Tayssir',email='taysir.boubaker@gmail.com' )
        self.account_manager = MyAccountManager()
        self.account = Account.objects.create(username='Tayssir',email='taysir.boubaker@gmail.com' )

    def test_account_manger_model(self):
        d = self.account_manager
        self.assertTrue(isinstance(d, MyAccountManager))

        # Test create_user Fonction 

        user1 = Account.objects.create_user(username='Tayssir1',email='taysir1.boubaker@gmail.com')
        self.assertTrue(isinstance(user1, Account))
        
        with pytest.raises(ValueError):
            user2 = Account.objects.create_user(username='',email='taysir2.boubaker@gmail.com')

        with pytest.raises(ValueError):
            user3 = Account.objects.create_user(username='Tayssir3',email='')

        # Test create_user Fonction 
        super_user = Account.objects.create_superuser(username='Tati',email='tati.boubaker@gmail.com', password='tati')
        self.assertTrue(isinstance(super_user, Account))

    # Test Account 
    def test_account_model(self):
        d = self.account
        self.assertTrue(isinstance(d, Account))
        self.assertEqual(str(d), 'taysir.boubaker@gmail.com')
        self.assertEqual(d.has_perm('perm'), False)
        self.assertEqual(d.has_module_perms('app_label'), True)

    # TEST VIEW RegistrationForm

class User_Form_Test(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = RegistrationForm(data={'email': "tatixx.boubaker@gmail.com", 'username': "Hamster", 'password1': "GMC202120212021", 'password2': 'GMC202120212021'})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = RegistrationForm(data={'email': "user@mp.com", 'username': "user", 'password1': "tati", 'password2': 'tatifdjkjkj'})
        self.assertFalse(form.is_valid())

# TEST VIEW AccountAuthenticationForm

class User_Form_Test(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = AccountAuthenticationForm(data={'email': "tatixx.boubaker@gmail.com",'password': "GMC202120212021"})
        form.clean()
    # def test_UserForm_invavalid(self):
    #     form = AccountAuthenticationForm(data={'email': "hhhh",'password': "xxx"})
    #     with pytest.raises(forms.ValidationError):
    #         form.clean()

# TEST VIEW AccountUpdateForm
class User_Form_Test(TestCase):

    def test_UserForm_valid(self):
        form = AccountUpdateForm(data={'email': "tatixx.boubaker@gmail.com",'username': "Hamster"})
        form.clean_email()

    def test_UserForm_valid(self):
        form = AccountUpdateForm(data={'email': "tatixx.boubaker@gmail.com",'username': "Hamster"})
        form.clean_username()

    # def test_UserForm_valid(self):
    #     form = AccountUpdateForm(data={'email': "taysir.boubaker2082@gmail.com'",'username': "Tayssir"})
    #     form.clean_email()

    # def test_UserForm_valid(self):
    #     form = AccountUpdateForm(data={'email': "taysir.boubaker2082@gmail.com'",'username': "Tayssir"})
    #     form.clean_username()

class ViewTesting(TestCase):
    def test_home(self):
        c = Client()
        response = c.get('')
        # print (response.status_code)
        #print (response.content)

    def test_login(self):
        self.account = Account.objects.create(username='TayssirB',email='tayssir.boubaker@gmail.com' )
        c = Client()
        response = c.get('/login/')
        self.assertTemplateUsed(response, 'account/login.html')
        user_login = c.login(username=str(self.account), password='Walaboubaker')
        self.assertTrue(user_login)

        #print (response.status_code)
        response2 = c.post('/login/', {'email': 'taysir.boubaker2082@gmail.com', 'password': 'Walaboubaker'})
        print (response2.status_code)
        # print (response2.content)
        #self.assertRedirects(response2, 'home')


    ##THIS ONLY WHEN AUTHENTICATE
    def test_logout(self):
        c = Client()
        response = c.get('/logout/')
        # print (response.status_code)
        self.assertRedirects(response, '/')

    def test_account_view(self):
        c = Client()
        response = c.get('/account/')
        self.assertRedirects(response, '/login/')
        response2 = c.post('/login/', {'email': 'taysir.boubaker2082@gmail.com', 'password': 'Walaboubaker'})
        # c.login(email='taysir.boubaker2082@gmail.com', password='Walaboubaker')
        # response2 = c.get('/account/', follow=True)
        #print (response2.status_code)

    def test_register(self):
        c = Client()
        response = c.get('/register/')
        response2 = c.post('/register/', {'email': 'taysir33.boubaker2082@gmail.com','username' :'MAMAMIA', 'password1': '202120215698djdhhd', 'password2': '202120215698djdhhd'})
        response3 = c.post('/register/', {'email': 'taysir33.boubaker2082@gmail.com','username' :'MAMAMIA', 'password1': '202120215698djdhhd', 'password2': '20212021jgfdjd'})
        # print (response.status_code)
        

