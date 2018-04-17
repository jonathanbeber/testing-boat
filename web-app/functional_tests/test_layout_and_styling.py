from .base import FunctionalTest


class LayoutAndStyleTest(FunctionalTest):
    def test_layout_ans_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        input_box = self._get_input_box()
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            512,
            delta=10
        )
        self._set_new_item('new item')
        input_box = self._get_input_box()
        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            512,
            delta=10
        )
