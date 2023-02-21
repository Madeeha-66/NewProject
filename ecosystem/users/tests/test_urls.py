from django.test import SimpleTestCase
from django.urls import reverse , resolve
from users.views import register , logout_view
from django.contrib.auth.views import LoginView

class TestUrls(SimpleTestCase):
    def test_register_resolve(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func , register)

    def test_logout_resolve(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func , logout_view)
    def test_login_resolve(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class , LoginView)