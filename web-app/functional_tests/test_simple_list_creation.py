from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):
    def test_include_a_list_and_get_a_permanent_link(self):
        # Enter the site
        self.browser.get(self.live_server_url)

        # check the site's title
        self.assertIn('To-Do List', self.browser.title)

        # check the site header
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Start your new To-Do List', header_text)

        # check input box placeholder
        self.assertEqual(
            self._get_input_box().get_attribute('placeholder'),
            'insert a new item'
        )

        # Insert text 'buy milk' in the new item box
        first_task_text = 'buy milk'
        self._set_new_item(first_task_text)

        # Check if the item is in the page
        self._check_item('1. ' + first_task_text)

        # Insert new item 'Clean the car'
        second_task_text = 'Clean the car'
        self._set_new_item(second_task_text)

        # check if the new item is in the page
        self._check_item('1. ' + first_task_text)
        self._check_item('2. ' + second_task_text)


    def test_unique_url(self):
        # enter the site
        self.browser.get(self.live_server_url)

        # add a new item
        user_a_item_text = 'awesome new item'
        self._set_new_item(user_a_item_text)

        # check for the item
        self._check_item('1. ' + user_a_item_text)

        # Check the new url
        user_a_url = self.browser.current_url
        self.assertRegex(user_a_url, '/list/.+')

        ## create a new browser for test isolation
        self.browser.quit()
        self.browser = self._get_a_browser()

        # New user visits the site
        self.browser.get(self.live_server_url)

        # Add a new item
        user_b_item_text = 'some boring task'
        self._set_new_item(user_b_item_text)

        # check for the item
        self._check_item('1. ' + user_b_item_text)

        # check url
        self.assertRegex(self.browser.current_url, '/list/.+')
        self.assertNotEqual(self.browser.current_url, user_a_url)

        # Check for the user a's item again
        self.assertNotIn(
            '1. ' + user_a_item_text,
            [row.text for row in self._get_todo_rows()]
        )
