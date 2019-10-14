"""module for methods from locators"""
from locators.ProductsPageLocators import ProductPageLocators


class ProductsPage:
    """Class for methods for Products Page"""
    def __init__(self, driver):
        self.driver = driver

    def open_catalog(self):
        self.driver.find_element(*ProductPageLocators.CATALOG).click()

    def open_products(self):
        catalog_elements = self.driver.find_elements_by_tag_name("li")
        for catalog_element in catalog_elements:
            if catalog_element.text == "Products":
                catalog_element.click()
                break

    def
