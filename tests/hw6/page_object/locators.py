"""this file contains locators for web elements on pages"""
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for Main Page locators and also for locators which presented on every page"""
    TOP_MENU = (By.ID, "top")
    SEARCH_INPUT = (By.CSS_SELECTOR, ".form-control")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn-default")
    HOME = (By.CSS_SELECTOR, "#logo > h1:nth-child(1) > a:nth-child(1)")
    MENU_LINKS = (By.ID, "navbar-nav")
    DECKTOPS = (By.CSS_SELECTOR, "li.dropdown:nth-child(1) > a:nth-child(1)")
    LAPTOPS = (By.CSS_SELECTOR, "ul.nav > li:nth-child(2) > a:nth-child(1)")
    COMPONENTS = (By.CSS_SELECTOR, "ul.nav > li:nth-child(2) > a:nth-child(1)")
    TABLETS = (By.CSS_SELECTOR, "li.dropdown:nth-child(3) > a:nth-child(1)")
    SOFTWARE = (By.CSS_SELECTOR, "ul.nav > li:nth-child(5) > a:nth-child(1)")
    PHONES = (By.CSS_SELECTOR, "ul.nav > li:nth-child(6) > a:nth-child(1)")
    CAMERAS = (By.CSS_SELECTOR, "ul.nav > li:nth-child(7) > a:nth-child(1)")
    PLAYERS = (By.CSS_SELECTOR, "li.dropdown:nth-child(8) > a:nth-child(1)")
    CART = (By.CSS_SELECTOR, ".btn-inverse")
    BREADCRUMBS = (By.ID, "breadcrumbs")


class AdminLoginPageLocators(object):
    """A class for Admin Login Page locators"""
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, ".help-block > a:nth-child(1)")
    ERROR = (By.CLASS_NAME, "alert.alert-danger.alert-dismissible")
    BUTTON = (By.CLASS_NAME, "btn-primary")


class CatalogPageLocators(object):
    """A class for Catalog Page locators"""
    HOME = (By.CLASS_NAME, "fa-home")
    FILTER_SORT_BY = (By.ID, "input-sort")


class ProductPageLocators(object):
    """A class for Product Page locators"""
    ADD_TO_CART = (By.ID, "button-cart")
    COMPARE = (By.CLASS_NAME, "fa-exchange")
    ADD_TO_WL = (By.XPATH, "//button[@data-original-title='Add to Wish List']")
    ADDED_TO_WL = (By.CLASS_NAME, "alert")
    QUANTITY = (By.ID, "input-quantity")

