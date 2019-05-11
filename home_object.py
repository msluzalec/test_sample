import home_locators as locators
import requests


class HomePageObject:

    NAVIGATION_ITEMS = {
        locators.IMAGES: '//yandex.com/images',
        locators.VIDEO: '//yandex.com/video',
        locators.MAIL: 'https://mail.yandex.com',
        locators.MAPS: '//yandex.com/maps',
        locators.APPMETRICA: '//appmetrica.yandex.com',
        locators.TRANSLATE: '//translate.yandex.com',
        locators.BROWSER: '//browser.yandex.com'
    }

    def __init__(self, driver):
        self.driver = driver
        self.yandex_logo = self.driver.find_element_by_class_name(locators.YANDEX_LOGO)
        self.search_field = self.driver.find_element_by_class_name(locators.SEARCH_FIELD)
        self.keyboard_icon = self.driver.find_element_by_class_name(locators.KEYBOARD)

    def is_yandex_logo_displayed(self):
        return self.yandex_logo.is_displayed()

    def is_search_field_displayed(self):
        return self.search_field.is_displayed()

    def find_nav_item(self, nav_item):
        return self.driver.find_element_by_id(nav_item)

    @staticmethod
    def is_nav_item_displayed(nav_item):
        return nav_item.is_displayed()

    @staticmethod
    def get_nav_item_href(nav_item):
        return nav_item.get_attribute('href')

    @staticmethod
    def get_nav_item_link_status_code(nav_item_link):
        return requests.get(nav_item_link).status_code

    def is_keyboard_popup_displayed(self):
        return self.driver.find_element_by_class_name(
            locators.KEYBOARD_POPUP).is_displayed()
