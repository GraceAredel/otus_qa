"""main module for tests"""
import pytest

from locators.BaseLocators import BaseLocators
from page_objects.base_page import BasePage
from page_objects.admin_page import AdminPage


@pytest.fixture(scope="function")
def base_page(request, driver):
    """fixture for opening a page and declaring a driver"""
    driver.get(request.config.getoption("--address"))
    return BasePage(driver)


@pytest.fixture(scope="function")
def admin_page(request, driver):
    """fixture for opening a page and declaring a driver"""
    driver.get(request.config.getoption("--address") + "admin/")
    return AdminPage(driver)


@pytest.mark.usefixtures("base_page")
class TestBase:
    """tests for functions that present on main page
    and all pages at the same time"""

    def test_your_store_exists(self, base_page):
        """check that your store button presents on base page"""
        assert base_page._get_element(*BaseLocators.HOME)

    def test_search(self, base_page):
        """searching test"""
        base_page.fill_search_input("iphone")
        base_page.click_search_button()
        h4 = base_page._get_element(*BaseLocators.H4)
        assert h4.text == "iPhone"

    def test_add_to_cart(self, base_page):
        """add item to cart and check it was added"""
        base_page.open_main_page()
        base_page.fill_search_input("iphone")
        base_page.click_search_button()
        base_page.add_to_cart()
        alert = base_page.find_alert()
        assert alert.text == "Success: You have added " \
                             "iPhone to your shopping cart!\n×"


@pytest.mark.usefixtures("admin_page")
@pytest.mark.usefixtures("base_page")
class TestsLogin:
    """tests for admin page"""

    def test_admin_login(self, admin_page, base_page,
                         login="user", password="bitnami1"):
        """test to check login function"""
        admin_page.login(login, password)
        h1 = base_page._get_element(*BaseLocators.H1)
        assert h1.text == "Dashboard"

