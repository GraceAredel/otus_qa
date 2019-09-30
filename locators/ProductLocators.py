"""this file contains locators for web elements on pages"""
from selenium.webdriver.common.by import By


class ProductLocators(object):
    """A class for Product Page locators"""
    ADD_TO_CART = (By.ID, "button-cart")
    COMPARE = (By.CLASS_NAME, "fa-exchange")
    ADD_TO_WL = (By.XPATH, "//button[@data-original-title='Add to Wish List']")
    ADDED_TO_WL = (By.CLASS_NAME, "alert")
    QUANTITY = (By.ID, "input-quantity")
