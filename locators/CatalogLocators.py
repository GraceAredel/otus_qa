"""this file contains locators for web elements on pages"""
from selenium.webdriver.common.by import By


class CatalogLocators(object):
    """A class for Catalog Page locators"""
    HOME = (By.CLASS_NAME, "fa-home")
    FILTER_SORT_BY = (By.ID, "input-sort")
