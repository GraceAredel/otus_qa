"""this file contains locators for web elements on pages"""
from selenium.webdriver.common.by import By


class AdminLocators(object):
    """A class for Admin Login Page locators"""
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    EMAIL = (By.ID, "input-email")
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, ".help-block > a:nth-child(1)")
    BUTTON = (By.CLASS_NAME, "btn-primary")
    RESET_BUTTON = (By.CLASS_NAME, "fa-check")
