from django.urls import resolve
from django.test import TestCase

from lists.views import home_page


class HomePageTest(TestCase):
    def test_html_format(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
