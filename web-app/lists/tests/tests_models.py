from django.urls import resolve
from django.test import TestCase
from django.core.exceptions import ValidationError

from lists.models import Item, List

class ItemListModelsTest(TestCase):
    def test_list_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), f'/list/{list_.id}/')

    def test_item_save(self):
        first_list = List()
        first_list.save()

        first_item = Item()
        first_item.list = first_list
        first_item.text = 'Do some really important stuff'
        first_item.save()

        second_item = Item()
        second_item.list = first_list
        second_item.text = 'Do another really important stuff'
        second_item.save()

        self.assertEqual(first_list, List.objects.first())

        items = Item.objects.all()
        self.assertEqual(items.count(), 2)

        first_saved_item = items[0]
        second_saved_item = items[1]

        self.assertEqual(first_list, first_saved_item.list)
        self.assertEqual(first_item.text, first_saved_item.text)
        self.assertEqual(first_list, second_saved_item.list)
        self.assertEqual(second_item.text, second_saved_item.text)


    def test_cannot_save_empty_item(self):
        _list = List()
        _list.save()

        item = Item()
        item.list = _list
        item.text = ''
        with self.assertRaises(ValidationError):
            item.full_clean()
            item.save()
