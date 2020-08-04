"""module for methods from locators"""
import time

from selenium.webdriver.common.action_chains import ActionChains

from locators.CatalogPageLocators import CatalogPageLocators
from page_objects.base_page import BasePage


class CatalogPage(BasePage):
    """Class for methods for Products Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_catalog(self):
        self.driver.find_element(*CatalogPageLocators.CATALOG).click()

    def open_products_page(self):
        catalog_elements = self.driver.find_elements_by_tag_name("li")
        for catalog_element in catalog_elements:
            if catalog_element.text == "Products":
                catalog_element.click()
                break

    def open_downloads_page(self):
        catalog_elements = self.driver.find_elements_by_tag_name("li")
        for catalog_element in catalog_elements:
            if catalog_element.text == "Downloads":
                catalog_element.click()
                break

    def click_add_new(self):
        self.driver.find_element(*CatalogPageLocators.ADD_NEW).click()

    def click_edit_product(self):
        self.driver.find_element(*CatalogPageLocators.EDIT).click()

    def click_delete_product(self):
        self.driver.find_element(*CatalogPageLocators.DELETE).click()

    def click_save_changes(self):
        self.driver.find_element(*CatalogPageLocators.SAVE).click()

    def click_filter_button(self):
        btn = self.driver.find_elements(*CatalogPageLocators.FILTER)
        btn[2].click()

    def fill_product_name_filter(self, keys):
        element = self.driver.find_element(*CatalogPageLocators.PRODUCT_NAME_FILTER)
        ActionChains(self.driver).send_keys_to_element(element, keys).perform()

    def fill_product_name_field(self, keys):
        element = self.driver.find_element(*CatalogPageLocators.PRODUCT_NAME)
        ActionChains(self.driver).send_keys_to_element(element, keys).perform()

    def fill_meta_tag_title_field(self, keys):
        element = self.driver.find_element(*CatalogPageLocators.META_TAG_TITLE)
        ActionChains(self.driver).send_keys_to_element(element, keys).perform()

    def clear_product_name_field(self):
        self._find_and_clear_element(*CatalogPageLocators.PRODUCT_NAME)

    def open_data_tab(self):
        self._wait_element(*CatalogPageLocators.DATA_TAB)
        self.driver.find_element(*CatalogPageLocators.DATA_TAB).click()

    def open_image_tab(self):
        self._wait_element_clickable(*CatalogPageLocators.IMAGE_TAB)
        self.driver.find_element(*CatalogPageLocators.IMAGE_TAB).click()

    def select_logo(self):
        self.driver.find_element(*CatalogPageLocators.LOGO).click()

    def fill_model_name_field(self, keys):
        element = self.driver.find_element(*CatalogPageLocators.MODEL_NAME)
        ActionChains(self.driver).send_keys_to_element(element, keys).perform()

    def click_in_checkbox(self):
        self.driver.find_element(*CatalogPageLocators.CHECKBOX).click()

    def create_new_product(self, name, meta, model):
        self.open_catalog()
        self.open_products_page()
        self._wait_element_clickable(*CatalogPageLocators.ADD_NEW, 5)
        self.click_add_new()
        self.fill_product_name_field(name)
        self.fill_meta_tag_title_field(meta)
        self.open_data_tab()
        self.fill_model_name_field(model)
        self.click_save_changes()
        time.sleep(3)
        alert = self.find_alert()
        assert alert.text == "Success: You have modified products!\n×"

    def click_upload_button(self):
        self.driver.find_element(*CatalogPageLocators.UPLOAD).click()

    def send_filename(self, filename):
        file = self.driver.find_element(*CatalogPageLocators.FILE)
        file.send_keys(filename)

    def set_download_name(self, name):
        self.driver.find_element(*CatalogPageLocators.DOWNLOAD_NAME).send_keys(name)

    def set_mask(self, mask):
        self.driver.find_element(*CatalogPageLocators.MASK).send_keys(mask)

    # def upload_file_script(self, filename):
    #     fileinput = self.driver.find_element(*CatalogPageLocators.FILE)
    #     self.driver.execute_script(
    #         'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
    #         fileinput)
    #     fileinput.send_keys(filename)

    def upload_file_script(self, filename):
        self.driver.execute_script('document.querySelector("#image0").setAttribute("value", filename)')
        self.driver.find_element_by_css_selector("#form-upload").click()
