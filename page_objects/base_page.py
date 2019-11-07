"""module for methods from locators"""
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException

from locators.BaseLocators import BaseLocators


class BasePage:
    """Base class for methods that could be called from main page and top menu"""

    def __init__(self, driver):
        self.driver = driver

    def _get_element(self, *locator):
        return self.driver.find_element(*locator)

    def _wait_element(self, by, value, delay=25):
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((by, value)))
            element = self.driver.find_element(by, value)
            return element
        except (NoSuchElementException, TimeoutException):
            return False

    def _wait_element_clickable(self, by, value, delay=25):
        try:
            WebDriverWait(self.driver, delay).until(EC.element_to_be_clickable((by, value)))
            element = self.driver.find_element(by, value)
            return element
        except ElementNotInteractableException:
            return False

    def _find_and_clear_element(self, by, value):
        element = self.driver.find_element(by, value)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACK_SPACE)

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
        return self.driver.find_element(*BaseLocators.ALERT)

    def accept_alert(self):
        obj = self.driver.switch_to.alert
        obj.accept()

    def find_in_page_source(self, text):
        html_source = self.driver.page_source
        if text in html_source:
            return True
        else:
            return False
