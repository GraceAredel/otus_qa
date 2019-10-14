"""this file contains locators for web elements on pages"""
from selenium.webdriver.common.by import By


class ProductPageLocators(object):

    CATALOG = (By.CLASS_NAME, "parent.collapsed")
    ADD_NEW = (By.CLASS_NAME, "fa-plus")
    DELETE = (By.CLASS_NAME, "fa-trash-o")
    EDIT = (By.CLASS_NAME, "fa-pencil")
    SAVE = (By.CLASS_NAME, "fa-save")

