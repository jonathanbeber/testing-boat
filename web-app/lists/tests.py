from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_is_routing_rigth(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_html_format(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startwith('<html>'))
        self.assertIn('<title>To-do List</title>', html)
        self.assertTrue(html.endswith('</html>'))
