from urllib import parse
import logging
from datetime import datetime

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
    logger = logging.getLogger("otus_qa")
    logger.setLevel(logging.DEBUG)
    now = datetime.now().strftime("%Y%m%d-%Hh%M")
    log_file = "./logs/" + now + ".log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    handler_format = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
    file_handler.setFormatter(handler_format)
    console_handler.setFormatter(handler_format)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


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

    yield wd
    wd.quit()


@pytest.fixture(scope="session")
def opencart(request):
    return request.config.getoption("--address")


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
