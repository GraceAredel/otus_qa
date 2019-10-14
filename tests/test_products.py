"""module for products page tests"""
import pytest

from locators.ProductsPageLocators import ProductPageLocators


@pytest.fixture(scope="function")
def admin_page(request, driver):
    """fixture for opening a page and declaring a driver"""
    driver.get(request.config.getoption("--address") + "admin/")
    return AdminPage(driver)


@pytest.mark.usefixtures("login")


