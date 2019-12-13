"""main module for tests"""
import logging
import allure
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver, AbstractEventListener

from locators.BaseLocators import BaseLocators
from page_objects.base_page import BasePage
from page_objects.admin_page import AdminPage


@allure.description("fixture for opening a page and declaring a driver")
@pytest.fixture(scope="function")
def base_page(request, driver):
    driver.get(request.config.getoption("--address"))
    return BasePage(driver)


@allure.description("fixture for opening a page and declaring a driver")
@pytest.fixture(scope="function")
def admin_page(request, driver):
    driver.get(request.config.getoption("--address") + "admin/")
    return AdminPage(driver)


@allure.description("fixture for declaring a EFwebdriver")
@pytest.fixture
def firefox_browser(request):
    ff_wd = EventFiringWebDriver(webdriver.Firefox(), MyListener())
    request.addfinalizer(ff_wd.quit)
    return ff_wd


class MyListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        screenshot_name = "exception.png"
        driver.get_screenshot_as_file(screenshot_name)
        print(f"Screenshot saved as {screenshot_name}")
        print(exception)


@allure.description("tests for functions that present "
                    "on main page and all pages at the same time")
@pytest.mark.usefixtures("base_page")
class TestBase:

    @allure.description("check that your store button presents on base page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_your_store_exists(self, base_page):
        assert base_page._get_element(*BaseLocators.HOME)

    @allure.description("""searching test""")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search(self, base_page):
        base_page.fill_search_input("iphone")
        base_page.click_search_button()
        h4 = base_page._get_element(*BaseLocators.H4)
        assert h4.text == "iPhone"

    @allure.description("add item to cart and check it was added")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_to_cart(self, base_page):
        with allure.step("open main page"):
            base_page.open_main_page()
        with allure.step("search"):
            base_page.fill_search_input("iphone")
            base_page.click_search_button()
        with allure.step("add to cart"):
            base_page.add_to_cart()
        alert = base_page.find_alert()
        assert alert.text == "Success: You have added " \
                             "iPhone to your shopping cart!\n×"


@allure.description("tests for admin page")
@pytest.mark.usefixtures("logger")
@pytest.mark.usefixtures("admin_page")
@pytest.mark.usefixtures("base_page")
class TestsLogin:
    @allure.description("test to check login function")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_admin_login(self, admin_page, base_page,
                         login="user", password="bitnami1"):
        with allure.step("login"):
            admin_page.login(login, password)
        logger = logging.getLogger("otus_qa")
        h1 = base_page._get_element(*BaseLocators.H1)
        with allure.step("assertion"):
            assert h1.text == "Dashboard"
        logger.info("User successfully logged in")


@allure.description("""try to find non-existing element,
                    then make a screenshot of an error""")
@allure.severity(allure.severity_level.MINOR)
def test_raise_listener_error(firefox_browser):
    try:
        firefox_browser.find_element(*BaseLocators.NON_EXISTING_ELEMENT)
    except NoSuchElementException:
        pytest.xfail("controlling fail")
