"""module for methods from locators"""
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

    def fill_product_name_field(self, keys):
        element = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys(keys)
        actions.perform()

    def fill_meta_tag_title_field(self, keys):
        element = self.driver.find_element(ProductPageLocators.META_TAG_TITLE)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys(keys)
        actions.perform()

    def clear_product_name_field(self):
        self._find_and_clear_element(*ProductPageLocators.PRODUCT_NAME)

    def open_data_tab(self):
        self.driver.find_element(*ProductPageLocators.DATA_TAB)

    def fill_model_name_field(self, keys):
        element = self.driver.find_element(*ProductPageLocators.MODEL_NAME)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys(keys)
        actions.perform()

    def click_in_checkbox(self):
        self.driver.find_element(*ProductPageLocators.CHECKBOX).click()
