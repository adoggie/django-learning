#coding:utf-8

django.test.Client
 	具有restful, post-file所有调用接口

#基本的http请求
    from django.test import Client
    c = Client()
    response = c.post('/login/', {'username': 'john', 'password': 'smith'})
    response.status_code
    response = c.get('/customer/details/')
    response.content

#上传文件测试
    c = Client()
    with open('wishlist.doc') as fp:
       c.post('/customers/wishes/', {'name': 'fred', 'attachment': fp})


from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from .views import MyView, my_view

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user( username='jacob', email='jacob@…', password='top_secret')

    def test_details(self):
        request = self.factory.get('/customer/details')


from django.test import TestCase
from myapp.models import Animal

class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        cat = Animal.objects.get(name="cat")
        self.assertEqual(cat.speak(), 'The cat says "meow"')

# Run all the tests in the animals.tests module
manage.py test animals.tests
manage.py test
manage.py test --pattern="tests_*.py"

