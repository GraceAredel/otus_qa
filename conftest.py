import pytest
from selenium import webdriver
from urllib import parse

from page_objects.admin_page import AdminPage


def pytest_addoption(parser):
    parser.addoption("--address", action="store",
                     default="http://localhost/opencart/",
                     help="Opencard address")
    parser.addoption("--browser", action="store",
                     default="firefox", help="Browser name")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        wd = webdriver.Firefox()
        wd.maximize_window()
    elif browser == 'chrome':
        wd = webdriver.Chrome()
    else:
        print("Internet Explorer is a crap!")
        wd = webdriver.Ie()

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
