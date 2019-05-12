from base_test_case import BaseTestCase
from home_object import HomePageObject
import unittest


class HomeTestCases(BaseTestCase):
    url = "https://www.yandex.com"
    page_object_class = HomePageObject

    def test_yandex_logo(self):
        self.assertTrue(self.page_object.is_yandex_logo_displayed(),
                        "Yandex logo is not displayed")

    def test_search_field(self):
        self.assertTrue(self.page_object.is_search_field_displayed(),
                        "Search field is not displayed")

    def test_navigation_items(self):
        for nav_item, expected_link in self.page_object.NAVIGATION_ITEMS.items():
            navigation_item = self.page_object.find_nav_item(nav_item)
            self.assertTrue(self.page_object.is_nav_item_displayed(navigation_item),
                            "{0} is not displayed".format(nav_item))
            nav_item_link = self.page_object.get_nav_item_href(navigation_item)
            self.assertIn(expected_link, nav_item_link,
                          "There is wrong expected_link for {0}".format(nav_item))
            self.assertEqual(
                self.page_object.get_nav_item_link_status_code(nav_item_link), 200,
                "There is wrong status code for {0}".format(nav_item))

    def test_keyboard_icon(self):
        self.page_object.remove_cookie_banner()
        self.page_object.keyboard_icon.click()
        self.assertTrue(self.page_object.is_keyboard_popup_displayed(),
                        "Keyboard popup did not show after clicking keyboard icon")
        self.page_object.close_keyboard_popup()


if __name__ == "__main__":
    unittest.main()
