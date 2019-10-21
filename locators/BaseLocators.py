"""this file contains locators for web elements on pages"""
from selenium.webdriver.common.by import By


class BaseLocators(object):
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
    ADD_TO_CART = (By.CLASS_NAME, "fa-shopping-cart")
    ALERT = (By.CLASS_NAME, "alert-success")
    H4 = (By.TAG_NAME, "h4")
    H1 = (By.TAG_NAME, "h1")

