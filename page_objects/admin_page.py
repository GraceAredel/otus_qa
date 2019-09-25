"""module for functions from locators"""
from locators.admin import AdminLocators


class AdminPage:
    """base class for methods on admin page"""

    def __init__(self, driver):
        self.driver = driver

    def login(self, login, password):
        self.driver.find_element(*AdminLocators.USERNAME).send_keys(login)
        self.driver.find_element(*AdminLocators.PASSWORD).send_keys(password)
        self.driver.find_element(*AdminLocators.BUTTON).click()

    def reset_password(self, email):
        self.driver.find_element(*AdminLocators.FORGOTTEN_PASSWORD).click()
        self.driver.find_element(*AdminLocators.EMAIL).send_keys(email)
