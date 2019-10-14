import pytest
from selenium import webdriver

from page_objects.admin_page import AdminPage


def pytest_addoption(parser):
    parser.addoption("--address", action="store",
                     default="http://127.0.0.1/opencart/",
                     help="Opencard address")
    parser.addoption("--browser", action="store",
                     default="firefox", help="Browser name")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        wd = webdriver.Firefox()
    elif browser == 'chrome':
        wd = webdriver.Chrome()
    else:
        print("Internet Explorer is a crap!")
        wd = webdriver.Ie()

    request.addfinalizer(wd.quit)
    wd.get(request.config.getoption("--address"))

    return wd


@pytest.fixture(scope="session")
def opencart(request):
    return request.config.getoption("--address")


@pytest.fixture(scope="session")
def login(driver, request):
    """login to admin page"""
    url = request.config.getoption("--address") + 'admin/'
    driver.get(url)
    admin_page = AdminPage(driver)
    admin_page.login(login="admin", password="moonlight")
