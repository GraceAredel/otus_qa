"""module for products page tests"""
import pytest
import time

from page_objects.products_page import ProductsPage


@pytest.fixture(scope="function")
def products_page(request, driver, login):
    """fixture for opening a page and declaring a driver"""
    url = request.config.getoption("--address") + "admin/index.php?route=catalog/product" + "&user_token=" + login
    print(url)
    driver.get(url)
    return ProductsPage(driver)

# def add_token(url, login):
#     parsed = parse.urlparse(url)
#     qs = {key: value[0] for key, value in qs.items() if len(value) == 1}
#     qs['user_token'] = login
#     new_url = parsed._replace(query=parse.urlencode(qs))
#     print(parse.urlunparse(new_url))
#     assert False
#     return parse.urlunparse(new_url)


@pytest.mark.usefixtures("products_page")
class TestProductsPage:
    """tests for products page"""

    def test_add_product(self, products_page):
        """test for new product creation"""
        products_page.create_new_product("new product", "new meta tag", "new model")
        alert = products_page.find_alert()
        assert alert.text == "Success: You have modified products!\n×"

    def test_change_product(self, products_page):
        """here i will create a new product first, then change it
        - to not overusing the existing products"""
        products_page.create_new_product("new product to edit", "gibberish", "new model")
        alert = products_page.find_alert()
        assert alert.text == "Success: You have modified products!\n×"
        products_page.fill_product_name_field("new product to edit")
        products_page.click_filter_button()
        products_page.click_edit_product()
        products_page.fill_meta_tag_title_field("new tag")
        products_page.click_save_changes()
        alert = products_page.find_alert()
        assert alert.text == " Success: You have modified products!\n×"

    def test_delete_product(self, products_page):
        """here i will create a new product first, then delete it,
        then try to find deleted product and make sure there are nothing"""
        products_page.create_new_product("delete me", "delete me", "delete me")
        alert = products_page.find_alert()
        assert alert.text == "Success: You have modified products!\n×"
        products_page.fill_product_name_field("delete me")
        products_page.click_filter_button()
        products_page.click_in_checkbox()
        products_page.click_delete_product()
        products_page.switch_to.alert.accept()
        alert = products_page.find_alert()
        assert alert.text == " Success: You have modified products!\n×"
        products_page.fill_product_name_field("delete me")
        products_page.click_filter_button()
        assert "No results!" in products_page.page_source

