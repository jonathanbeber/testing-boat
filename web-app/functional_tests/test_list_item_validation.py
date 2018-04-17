from unittest import skip

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_not_accept_empty_items(self):
        # Enter the site
        self.browser.get(self.live_server_url)

        # Try to insert an empty item
        self._set_new_item('')

        # Get an error message
        self.assertEqual(
            self._get_item_by_id('error-message').text,
            'Invalid item'
        )

        # Try with a valid item
        valid_item = 'valid item'
        self._set_new_item(valid_item)
        self._check_item('1. ' + valid_item)


        # Try insert an empty item again
        self._set_new_item(' ')


        # Get the same error message
        self.assertEqual(
            self._get_item_by_id('error-message').text,
            'Invalid item'
        )

        # include a new valid item and its ok
        valid_item = 'valid item #2'
        self._set_new_item(valid_item)
        self._check_item('2. ' + valid_item)
