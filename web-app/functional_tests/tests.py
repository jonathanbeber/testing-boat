import os
import time

from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome('/home/developer/chromedriver', options=options)


    def tearDown(self):
        self.browser.quit()


    def test_include_a_list_and_get_a_permanent_link(self):
        def _get_input_box():
            return self.browser.find_element_by_id("new-item-box")


        def _set_new_item(text):
            input_box = _get_input_box()
            input_box.send_keys(text)
            input_box.send_keys(Keys.ENTER)
            time.sleep(1)


        def _check_item(text):
            todo_list = self.browser.find_element_by_id('todo-list')
            rows = todo_list.find_elements_by_tag_name('tr')
            self.assertIn(text, [row.text for row in rows])

        # Enter the site
        self.browser.get(self.live_server_url)

        # check the site's title
        self.assertIn('To-Do List', self.browser.title)

        # check the site header
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do List', header_text)

        # check input box placeholder
        self.assertEqual(
            _get_input_box().get_attribute('placeholder'),
            'insert a new item'
        )

        # Insert text 'buy milk' in the new item box
        first_task_text = 'buy milk'
        _set_new_item(first_task_text)

        # Check if the item is in the page
        _check_item('1. ' + first_task_text)

        # Insert new item 'Clean the car'
        second_task_text = 'Clean the car'
        _set_new_item(second_task_text)

        # check if the new item is in the page
        _check_item('1. ' + first_task_text)
        _check_item('2. ' + second_task_text)

        self.fail('Finish it!')
        # Go to personal URL

        # check if 'buy milk' and 'Clean the car' are in a to-do list
