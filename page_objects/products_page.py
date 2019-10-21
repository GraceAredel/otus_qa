"""module for methods from locators"""
import time

from selenium.webdriver.common.action_chains import ActionChains

from locators.ProductsPageLocators import ProductPageLocators
from page_objects.base_page import BasePage


class ProductsPage(BasePage):
    """Class for methods for Products Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_catalog(self):
        self.driver.find_element(*ProductPageLocators.CATALOG).click()

    def open_products_page(self):
        catalog_elements = self.driver.find_elements_by_tag_name("li")
        for catalog_element in catalog_elements:
            if catalog_element.text == "Products":
                catalog_element.click()
                break

    def click_create_product(self):
        self.driver.find_element(*ProductPageLocators.ADD_NEW).click()

    def click_edit_product(self):
        self.driver.find_element(*ProductPageLocators.EDIT).click()

    def click_delete_product(self):
        self.driver.find_element(*ProductPageLocators.DELETE).click()

    def click_save_changes(self):
        self.driver.find_element(*ProductPageLocators.SAVE).click()

    def click_filter_button(self):
        btn = self.driver.find_elements(*ProductPageLocators.FILTER)
        btn[2].click()

    def fill_product_name_filter(self, keys):
        elements = self.driver.find_elements(*ProductPageLocators.PRODUCT_NAME_FILTER)
        ActionChains(self.driver).send_keys_to_element(elements[1], keys).perform()

    def fill_product_name_field(self, keys):
        element = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME)
        ActionChains(self.driver).send_keys_to_element(element, keys).perform()

    def fill_meta_tag_title_field(self, keys):
        element = self.driver.find_element(*ProductPageLocators.META_TAG_TITLE)
        ActionChains(self.driver).send_keys_to_element(element, keys).perform()

    def clear_product_name_field(self):
        self._find_and_clear_element(*ProductPageLocators.PRODUCT_NAME)

    def open_data_tab(self):
        self.driver.find_element(*ProductPageLocators.DATA_TAB).click()

    def fill_model_name_field(self, keys):
        element = self.driver.find_element(*ProductPageLocators.MODEL_NAME)
        ActionChains(self.driver).send_keys_to_element(element, keys).perform()

    def click_in_checkbox(self):
        self.driver.find_element(*ProductPageLocators.CHECKBOX).click()

    def create_new_product(self, name, meta, model):
        self.click_create_product()
        self.fill_product_name_field(name)
        self.fill_meta_tag_title_field(meta)
        self.open_data_tab()
        self.fill_model_name_field(model)
        self.click_save_changes()
        time.sleep(3)
        alert = self.find_alert()
        assert alert.text == "Success: You have modified products!\n×"
