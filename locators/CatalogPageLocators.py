"""this file contains locators for web elements on pages"""
from selenium.webdriver.common.by import By


class CatalogPageLocators(object):

    CATALOG = (By.CLASS_NAME, "parent.collapsed")
    ADD_NEW = (By.CLASS_NAME, "fa-plus")
    DELETE = (By.CLASS_NAME, "fa-trash-o")
    EDIT = (By.CLASS_NAME, "fa-pencil")
    SAVE = (By.CLASS_NAME, "fa-save")
    FILTER = (By.CLASS_NAME, "fa-filter")
    PRODUCT_NAME = (By.ID, "input-name1")
    META_TAG_TITLE = (By.ID, "input-meta-title1")
    DATA_TAB = (By.LINK_TEXT, "Data")
    IMAGE_TAB = (By.LINK_TEXT, "Image")
    MODEL_NAME = (By.NAME, "model")
    CHECKBOX = (By.NAME, "selected[]")
    PRODUCT_NAME_FILTER = (By.ID, "input-name")
    LOGO = (By.XPATH, "//input[@value='catalog/pic.jpg']")
    DOWNLOAD_NAME = (By.NAME, "download_description[1][name]")
    MASK = (By.NAME, "mask")
    UPLOAD = (By.ID, "button-upload")
    FILE = (By.CSS_SELECTOR, "input[type=file]")