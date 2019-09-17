from tests.hw6.page_object.locators import *


class BasePage:
    """Base class for methods that could be called from main page and top menu"""
    def __init__(self, driver):
        self.driver = driver

    def _get_element(self, *locator):
        return self.driver.find_element(*locator)

    def _fill_field(self, data, field):
        field.send_keys(data)
        return field

    def fill_search_input(self, text):
        search_field = self.driver.find_element(*MainPageLocators.SEARCH_INPUT)
        search_field.send_keys(text)

    def click_search_button(self):
        self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)

    def show_cart(self):
        self.driver.find_element(*MainPageLocators.CART)

    def open_main_page(self):
        your_store = self.driver.find_element(*MainPageLocators.HOME)
        your_store.click()


class LoginPage(BasePage):
    """base class for methods on login page"""
    def login(self, login, password):
        self.driver.find_element(*AdminLoginPageLocators.USERNAME).send_keys(login)
        self.driver.find_element(*AdminLoginPageLocators.PASSWORD).send_keys(password)
        self.driver.find_element(*AdminLoginPageLocators.BUTTON).click()

    def reset_password(self, email):
        self.driver.
        self.driver.find_element(*AdminLoginPageLocators.FORGOTTEN_PASSWORD)


