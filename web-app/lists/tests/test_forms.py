from django.test import TestCase

from lists.forms import ItemForm


class ItemFormTest(TestCase):
    def test_form_renders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="insert a new item"', form.as_p())
        self.assertIn('class="text-center form-control input-lg"', form.as_p())


    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        pass
        # self.fail('ch11l009')
        # self.assertFalse(form.is_valid())
        # self.assertEqual(
        #     form.errors.get('text'),
        #     ['Invalid item description']
        # )
