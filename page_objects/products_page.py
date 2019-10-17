"""module for methods from locators"""
from selenium.webdriver.common.action_chains import ActionChains

from locators.ProductsPageLocators import ProductPageLocators


class ProductsPage:
    """Class for methods for Products Page"""

    def __init__(self, driver):
        self.driver = driver

    def open_catalog(self):
        self.driver.find_element(*ProductPageLocators.CATALOG).click()

    def open_products_page(self):
        catalog_elements = self.driver.find_elements_by_tag_name("li")
        for catalog_element in catalog_elements:
            if catalog_element.text == "Products":
                catalog_element.click()
                break

    def edit_product(self):
        self.driver.find_element(*ProductPageLocators.EDIT).click()

    def delete_product(self):
        self.driver.find_element(*ProductPageLocators.DELETE).click()

    def save_changes(self):
        self.driver.find_element(*ProductPageLocators.SAVE).click()

    def click_filter_button(self):
        btn = self.driver.find_elements(*ProductPageLocators.FILTER)
        btn[2].click()

    def fill_product_name_field(self, keys):
        # self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).send_keys(keys)
        ActionChains(self).send_keys_to_element(*ProductPageLocators.PRODUCT_NAME,
                                                keys).perform()

    def meta_tag_edit(self, keys):
        ActionChains(self).send_keys_to_element(*ProductPageLocators.META_TAG,
                                                keys).perform()
