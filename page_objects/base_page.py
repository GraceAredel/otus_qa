"""module for functions from locators"""
from locators.BaseLocators import BaseLocators


class BasePage:
    """Base class for methods that could be called from main page and top menu"""

    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self):
        your_store = self.driver.find_element(*BaseLocators.HOME)
        your_store.click()

    def fill_search_input(self, text):
        search_field = self.driver.find_element(*BaseLocators.SEARCH_INPUT)
        search_field.send_keys(text)

    def click_search_button(self):
        self.driver.find_element(*BaseLocators.SEARCH_BUTTON).click()

    def show_cart(self):
        self.driver.find_element(*BaseLocators.CART).click()

    def add_to_cart(self):
        add = self.driver.find_elements(*BaseLocators.ADD_TO_CART)
        add[2].click()

    def find_alert(self):
        self.driver.find_element(*BaseLocators.ALERT)
