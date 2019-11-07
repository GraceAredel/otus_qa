"""module for products page tests"""
import pytest
import time


@pytest.mark.usefixtures("products_page")
@pytest.mark.usefixtures("login")
class TestProductsPage:
    """tests for products page"""

    @pytest.mark.usefixtures("products_page")
    def test_add_product(self, products_page):
        """test for new product creation"""
        products_page.create_new_product("new product",
                                         "new meta tag", "new model")
        time.sleep(3)
        alert = products_page.find_alert()
        assert alert.text == "Success: You have modified products!\n×"

    @pytest.mark.usefixtures("refresh_page")
    @pytest.mark.usefixtures("products_page")
    def test_change_product(self, products_page):
        """here i will create a new product first, then change it
        - to not overusing the existing products"""
        products_page.create_new_product("new product to edit",
                                         "gibberish", "edit model")
        time.sleep(3)
        alert = products_page.find_alert()
        assert alert.text == "Success: You have modified products!\n×"
        products_page.fill_product_name_filter("new product to edit")
        products_page.click_filter_button()
        products_page.click_edit_product()
        products_page.fill_meta_tag_title_field("new tag")
        products_page.click_save_changes()
        time.sleep(3)
        alert = products_page.find_alert()
        assert alert.text == "Success: You have modified products!\n×"

    @pytest.mark.usefixtures("refresh_page")
    @pytest.mark.usefixtures("products_page")
    def test_delete_product(self, products_page):
        """here i will create a new product first, then delete it,
        then try to find deleted product and make sure there are nothing"""
        products_page.create_new_product("delete me", "delete me", "delete me")
        products_page.fill_product_name_filter("delete me")
        products_page.click_filter_button()
        products_page.click_in_checkbox()
        products_page.click_delete_product()
        products_page.accept_alert()
        time.sleep(3)
        alert = products_page.find_alert()
        assert alert.text == "Success: You have modified products!\n×"
        products_page.fill_product_name_filter("delete me")
        products_page.click_filter_button()
        products_page.find_in_page_source("No results!")
