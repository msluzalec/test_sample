# Third party modules
import requests

# Own
import home_locators as locators


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
        self.yandex_logo = self.driver.find(locators.YANDEX_LOGO)
        self.search_field = self.driver.find(locators.SEARCH_FIELD)
        self.search_button = self.driver.find(locators.SEARCH_BUTTON)
        self.keyboard_icon = self.driver.find(locators.KEYBOARD)
        self.cookie_got_it_button = self.driver.find(locators.COOKIE_GOT_IT, wait=True)

    def remove_cookie_banner(self):
        if self.cookie_got_it_button:
            self.cookie_got_it_button.click()

    def is_yandex_logo_displayed(self):
        return self.yandex_logo.is_displayed()

    def is_search_field_displayed(self):
        return self.search_field.is_displayed()

    def find_nav_item(self, nav_item):
        return self.driver.find(nav_item)

    @staticmethod
    def is_nav_item_displayed(nav_item):
        return nav_item.is_displayed()

    @staticmethod
    def get_nav_item_href(nav_item):
        return nav_item.attribute('href')

    @staticmethod
    def get_nav_item_link_status_code(nav_item_link):
        return requests.get(nav_item_link).status_code

    def is_keyboard_popup_displayed(self):
        return self.driver.find(
            locators.KEYBOARD_POPUP, wait=True, ttl=5).is_displayed()

    def close_keyboard_popup(self):
        self.driver.find(locators.KEYBOARD_POPUP_CLOSE).click()
        self.driver.find(locators.KEYBOARD_POPUP).until(
            lambda e: len(e) == 0, ttl=5)

    def get_position_title(self):
        position = self.driver.find(
            locators.POSITION_TITLES).until(lambda e: len(e) > 0)
        return position.get(0).attribute('textContent')
