"""module for products page tests"""
import pytest

from locators.ProductsPageLocators import ProductPageLocators
from page_objects.products_page import ProductsPage


@pytest.mark.usefixtures("login")
@pytest.fixture(scope="function")
def products_page(request, driver):
    """fixture for opening a page and declaring a driver"""
    driver.get(request.config.getoption("--address") + "admin/")  # fix this
    return ProductsPage(driver)


@pytest.mark.usefixtures("products_page")
class TestProductsPage:
    """tests for products page"""

    def test_add_product(self, products_page):

    def test_change_product(self, products_page, keys="iPhone"):
        products_page.fill_product_name_field(keys)
        products_page.click_filter_button()
        products_page.edit_product()
        products_page.meta_tag_edit(keys)
        products_page.save_changes()
    #     add checking methods and assertion

    def test_delete_product():
