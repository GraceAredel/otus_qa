from urllib import parse
import logging

import pytest
from selenium import webdriver

from page_objects.admin_page import AdminPage
from page_objects.catalog_page import CatalogPage


def pytest_addoption(parser):
    parser.addoption("--address", action="store",
                     default="https://localhost/",
                     help="Opencard address")
    parser.addoption("--browser", action="store",
                     default="firefox", help="Browser name")
    parser.addoption("--wait", action="store",
                     default=0, help="Waiting")


@pytest.fixture(scope="session")
def logger():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename="logs.log", filemode='w', level=logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')



@pytest.mark.usefixtures("logger")
@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    time_to_wait = request.config.getoption("--wait")
    if browser == 'firefox':
        wd = webdriver.Firefox()
        wd.maximize_window()
    elif browser == 'chrome':
        wd = webdriver.Chrome()
    else:
        logger.warning("Unsupported browser!")
        wd = webdriver.Ie()

    wd.implicitly_wait(time_to_wait)
    wd.get(request.config.getoption("--address"))

    return wd


@pytest.fixture(scope="session")
def opencart(request):
    return request.config.getoption("--address")


@pytest.mark.usefixtures("logger")
@pytest.fixture(scope="session")
def login(driver, request):
    """login to admin page"""
    url = request.config.getoption("--address") + 'admin/'
    driver.get(url)
    admin_page = AdminPage(driver)
    admin_page.login(login="user", password="bitnami1")
    current_url = driver.current_url
    parsed = parse.urlparse(current_url)
    parse.parse_qs(parsed.query)
    token = parse.parse_qs(parsed.query)['user_token'][0]
    logger.info("User has logged in!")
    return token


@pytest.mark.usefixtures("login")
def add_token(url, login):
    parsed = parse.urlparse(url)
    qs = parse.parse_qs(parsed.query)
    qs['user_token'] = login
    new_url = parsed._replace(query=parse.urlencode(qs))
    return parse.urlunparse(new_url)


# def add_token(url, login):
#     parsed = parse.urlparse(url)
#     qs = {key: value[0] for key, value in qs.items() if len(value) == 1}
#     qs['user_token'] = login
#     new_url = parsed._replace(query=parse.urlencode(qs))
#     print(parse.urlunparse(new_url))
#     assert False
#     return parse.urlunparse(new_url)


@pytest.mark.usefixtures("login")
@pytest.fixture(scope="function", autouse=True)
def catalog_page(request, driver, login):
    """fixture for opening a page and declaring a driver"""
    url = request.config.getoption("--address") + \
        "admin/index.php?route=common/dashboard" + "&user_token=" + login
    driver.get(url)
    return CatalogPage(driver)


@pytest.fixture(scope="function")
def refresh_page(driver):
    driver.refresh()
    yield
    driver.refresh()

