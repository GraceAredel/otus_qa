import pytest
from tests.hw6.base_methods import BasePage, AdminPage, MainPageLocators


@pytest.fixture(scope="function")
def base_page(request, driver):
    driver.get(request.config.getoption("--address"))
    return BasePage(driver)

@pytest.fixture(scope="function")
def admin_page(request, driver):
    driver.get(request.config.getoption("--address") + "/admin/")
    return AdminPage(driver)


class BaseTests:
    """tests for functions that present on main page and all pages at the same time"""
    @pytest.mark.usefixtures("base_page")
    def test_your_store_exists(self):
        """check that your store button presents on base page"""
        assert base_page.find_element(*MainPageLocators.HOME)

    def test_search(self):
        """searching test"""
        base_page.fill_search_input("iphone")
        base_page.click_search_button()
        h4 = base_page.find_element_by_tag_name("h4")
        assert h4.text == "iPhone"

    def test_add_to_cart(self, text="iPhone"):
        """add item to cart and check it was added"""
        base_page.open_main_page()
        base_page.fill_search_input("iphone")
        base_page.click_search_button()
        base_page.add_to_cart()
        alert = base_page.find_alert()
        assert alert.text == "Success: You have added iPhone to your shopping cart!\n×"


class LoginTests:
    """tests for admin page"""
    @pytest.mark.usefixtures("admin_page")
    def test_admin_login(self, login=):
        admin_page.login()




