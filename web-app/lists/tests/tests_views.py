from django.urls import resolve
from django.test import TestCase

from lists.views import home_page
from lists.models import Item, List


ERROR_MESSAGE = 'Invalid item description'


class HomePageTest(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


    def test_errors_in_home_page(self):
        response = self.client.post(f'/list/new', data={'new-item': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, ERROR_MESSAGE)


class ListViewTest(TestCase):
    def test_view_list(self):
        list_ = List.objects.create()
        response = self.client.get(f'/list/{list_.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')


    def test_just_list_items_are_displayed(self):
        first_item_text = 'item 1'
        second_item_text = 'item 2'

        first_list = List.objects.create()
        second_list = List.objects.create()

        self.client.post(f'/list/{first_list.id}/', data={'new-item': first_item_text})
        self.client.post(f'/list/{second_list.id}/', data={'new-item': second_item_text})

        first_list_content = self.client.get(f'/list/{first_list.id}/').content.decode()
        self.assertIn(first_item_text, first_list_content)
        self.assertNotIn(second_item_text, first_list_content)
        self.assertIn(
            second_item_text,
            self.client.get(f'/list/{second_list.id}/').content.decode()
        )


    def test_list_in_the_context(self):
        list_ = List.objects.create()
        response = self.client.get(f'/list/{list_.id}/')
        self.assertEqual(response.context['list'], list_)


    def test_new_items_in_the_list_cant_be_empty(self):
        list_ = List.objects.create()
        response = self.client.post(f'/list/{list_.id}/', data={'new-item': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')
        self.assertContains(response, ERROR_MESSAGE)


class AddItemTest(TestCase):
    def test_POST_save_items(self):
        new_item_text = 'buy milk'
        list_ = List.objects.create()
        response = self.client.post(f'/list/{list_.id}/', data={'new-item': new_item_text})
        self.assertEqual(Item.objects.count(), 1)

        new_item = Item.objects.first()
        self.assertEqual(new_item.text, new_item_text)


    def test_redirect_after_POST(self):
        response = self.client.post(f'/list/new', data={'new-item': 'buy milk'})
        list_ = List.objects.first()
        self.assertRedirects(response, f'/list/{list_.id}/')
        response = self.client.post(f'/list/{list_.id}/', data={'new-item': 'buy milk 2'})
        self.assertRedirects(response, f'/list/{list_.id}/')


    def test_empty_items_arent_saved_when_creating_a_list(self):
        response = self.client.post(f'/list/new', data={'new-item': ''})
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)
