import os
import time

import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome('./chromedriver', options=options)
        self.host_address = os.environ.get('HOST_ADDRESS', 'localhost')


    def tearDown(self):
        self.browser.quit()


    def test_include_a_list_and_get_a_permanent_link(self):
        # Enter the site
        self.browser.get(
            'http://{}:8000'.format(self.host_address)
        )

        # check the site's title
        self.assertIn('To-Do', self.browser.title)

        self.fail('Finish it!')
        # Insert text 'buy milk' in the new item box

        # confirm the action

        # Check if the item is in the page

        # Insert new item 'Clean the car'

        # check if the new item is in the page

        # Go to personal URL

        # check if 'buy milk' and 'Clean the car' are in a to-do list


if __name__ == '__main__':
    unittest.main(warnings='ignore')
