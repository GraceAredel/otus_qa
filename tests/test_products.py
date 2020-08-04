"""module for products page tests"""
import pytest
import time


@pytest.mark.usefixtures("catalog_page")
@pytest.mark.usefixtures("login")
class TestProductsPage:
    """tests for products page"""

    @pytest.mark.usefixtures("catalog_page")
    def test_create_new_product(self, catalog_page):
        """test for new product creation"""
        catalog_page.create_new_product("new product",
                                        "new meta tag", "new model")
        # logo method here
        time.sleep(3)
        alert = catalog_page.find_alert()
        assert alert.text == "Success: You have modified products!\n×"

    @pytest.mark.usefixtures("refresh_page")
    @pytest.mark.usefixtures("catalog_page")
    def test_change_product(self, catalog_page):
        """here i will create a new product first, then change it
        - to not overusing the existing products"""
        catalog_page.create_new_product("new product to edit",
                                        "gibberish", "edit model")
        time.sleep(3)
        alert = catalog_page.find_alert()
        assert alert.text == "Success: You have modified products!\n×"
        catalog_page.fill_product_name_filter("new product to edit")
        catalog_page.click_filter_button()
        catalog_page.click_edit_product()
        catalog_page.fill_meta_tag_title_field("new tag")
        catalog_page.click_save_changes()
        time.sleep(3)
        alert = catalog_page.find_alert()
        assert alert.text == "Success: You have modified products!\n×"

    @pytest.mark.usefixtures("refresh_page")
    @pytest.mark.usefixtures("catalog_page")
    def test_delete_product(self, catalog_page):
        """here i will create a new product first, then delete it,
        then try to find deleted product and make sure there are nothing"""
        catalog_page.create_new_product("delete me", "delete me", "delete me")
        catalog_page.fill_product_name_filter("delete me")
        catalog_page.click_filter_button()
        catalog_page.click_in_checkbox()
        catalog_page.click_delete_product()
        catalog_page.accept_alert()
        time.sleep(3)
        alert = catalog_page.find_alert()
        assert alert.text == "Success: You have modified products!\n×"
        catalog_page.fill_product_name_filter("delete me")
        catalog_page.click_filter_button()
        catalog_page.find_in_page_source("No results!")
