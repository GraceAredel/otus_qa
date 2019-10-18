"""module for products page tests"""
import pytest

from locators.ProductsPageLocators import ProductPageLocators
from page_objects.products_page import ProductsPage


@pytest.fixture(scope="function")
def products_page(request, driver, login):
    """fixture for opening a page and declaring a driver"""
    driver.get(add_token(request.config.getoption("--address") +
               "admin/index.php?route=catalog/product&user_token=" + login)
    return ProductsPage(driver)


@pytest.mark.usefixtures("login")
@pytest.mark.usefixtures("products_page")
class TestProductsPage:
    """tests for products page"""

    def test_add_product(self, products_page):
        """test for new product creation"""
        products_page.click_create_product()
        products_page.fill_product_name_field(keys="new product")
        products_page.fill_meta_tag_field(keys="new meta tag")
        products_page.open_data_tab()
        products_page.fill_model_name_field(keys="new model")
        products_page.click_save_changes()
        alert = products_page.find_alert()
        assert alert.text == "Success: You have modified products!\n×"

    def test_change_product(self, products_page):
        """here i will create a new product first, then change it
        - to not overusing the existing products"""
        products_page.click_create_product()
        products_page.fill_product_name_field(keys="new product to edit")
        products_page.fill_meta_tag_field(keys="gibberish")
        products_page.open_data_tab()
        products_page.fill_model_name_field(keys="totally new model")
        products_page.click_save_changes()
        alert = products_page.find_alert()
        assert alert.text == "Success: You have modified products!"
        products_page.fill_product_name_field(keys="new product to edit")
        products_page.click_filter_button()
        products_page.click_edit_product()
        # probably i will need to scroll this element to view?
        products_page.fill_meta_tag_field(keys="new tag")
        products_page.click_save_changes()
        alert = products_page.find_alert()
        assert alert.text == " Success: You have modified products!\n×"

    def test_delete_product(self, products_page):
        """here i will create a new product first, then delete it,
        then try to find deleted product and make sure there are nothing"""
        products_page.click_create_product()
        products_page.fill_product_name_field(keys="delete me")
        products_page.fill_meta_tag_field(keys="delete me")
        products_page.open_data_tab()
        products_page.fill_model_name_field(keys="delete me")
        products_page.click_save_changes()
        alert = products_page.find_alert()
        assert alert.text == "Success: You have modified products!"
        products_page.fill_product_name_field(keys="delete me")
        products_page.click_filter_button()
        products_page.click_in_checkbox()
        products_page.click_delete_product()
        products_page.switch_to.alert.accept()
        alert = products_page.find_alert()
        assert alert.text == " Success: You have modified products!\n×"
        products_page.fill_product_name_field(keys="delete me")
        products_page.click_filter_button()
        assert "No results!" in products_page.page_source

