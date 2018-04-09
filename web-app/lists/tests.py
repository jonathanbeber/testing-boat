from django.urls import resolve
from django.test import TestCase

from lists.views import home_page

from lists.models import Item


class HomePageTest(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class ListViewTest(TestCase):
    def test_view_list(self):
        response = self.client.get('/list/the-only-existing-list')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')


    def test_all_items_are_displayed(self):
        first_item_text = 'item 1'
        second_item_text = 'item 2'
        self.client.post('/list/the-only-existing-list/new_item', data={'new-item': first_item_text})
        self.client.post('/list/the-only-existing-list/new_item', data={'new-item': second_item_text})

        response_text = self.client.get('/list/the-only-existing-list').content.decode()
        self.assertIn(first_item_text, response_text)
        self.assertIn(second_item_text, response_text)


class AddItemTest(TestCase):
    def test_POST_save_items(self):
        new_item_text = 'buy milk'
        response = self.client.post('/list/the-only-existing-list/new_item', data={'new-item': new_item_text})
        self.assertEqual(Item.objects.count(), 1)

        new_item = Item.objects.first()
        self.assertEqual(new_item.text, new_item_text)


    def test_redirect_after_POST(self):
        response = self.client.post('/list/the-only-existing-list/new_item', data={'new-item': 'buy milk'})
        self.assertRedirects(response, '/list/the-only-existing-list')


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
