import unittest
from selenium import webdriver
from elementium.drivers.se import SeElements


class BaseTestCase(unittest.TestCase):

    driver = None
    url = None
    page_object_class = None

    @classmethod
    def setUpClass(cls):
        cls.driver = SeElements(webdriver.Chrome(executable_path=r"C:\chromedriver.exe"))
        cls.driver.navigate(cls.url)
        cls.page_object = cls.page_object_class(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.browser.quit()
