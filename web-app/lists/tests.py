from django.urls import resolve
from django.test import TestCase

from lists.views import home_page

from lists.models import Item


class HomePageTest(TestCase):
    def test_html_format(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_handle_with_POST_requests(self):
        new_item_text = 'buy milk'
        response = self.client.post('/', data={'new-item': new_item_text})
        self.assertTemplateUsed(response, 'home.html')


class ItemTest(TestCase):
    def test_item_save(self):
        first_item = Item()
        first_item.text = 'Do some really important stuff'
        first_item.save()

        second_item = Item()
        second_item.text = 'Do another really important stuff'
        second_item.save()

        items = Item.objects.all()
        self.assertEqual(items.count(), 2)

        first_saved_item = items[0]
        second_saved_item = items[1]

        self.assertEqual(first_item.text, first_saved_item.text)
        self.assertEqual(second_item.text, second_saved_item.text)
