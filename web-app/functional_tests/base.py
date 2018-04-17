import os
import time

from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys


MAX_WAIT = 5


class FunctionalTest(LiveServerTestCase):
    def setUp(self):
        staging_url = os.environ.get('STAGING_URL')
        if staging_url:
            self.live_server_url = f'https://{staging_url}/'
        self.browser = self._get_a_browser()


    def _get_a_browser(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        return webdriver.Chrome('/home/developer/chromedriver', options=options)


    def tearDown(self):
        self.browser.quit()


    def _get_input_box(self):
        return self._get_item_by_id("new-item-box")


    def _get_item_by_id(self, id):
        return self.browser.find_element_by_id(id)


    def _set_new_item(self, text):
        input_box = self._get_input_box()
        input_box.send_keys(text)
        input_box.send_keys(Keys.ENTER)


    def _check_item(self, text):
        self.assertIn(
            text,
            [row.text for row in self._get_todo_rows()]
        )


    def _get_todo_rows(self):
        todo_list = self.browser.find_element_by_id('todo-list')
        return todo_list.find_elements_by_tag_name('tr')


    def _wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except(AssertionError, NoSuchElementException, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                else:
                    time.sleep(0.5)

