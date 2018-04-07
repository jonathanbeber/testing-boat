from django.urls import resolve
from django.test import TestCase

from lists.views import home_page


class HomePageTest(TestCase):
    def test_html_format(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_handle_with_POST_requests(self):
        new_item_text = 'buy milk'
        response = self.client.post('/', data={'new-item': new_item_text})
        self.assertTemplateUsed(response, 'home.html')
