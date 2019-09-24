import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://127.0.0.1/opencart/", help="Opencard address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")


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
        wd.quit()
    yield wd
    request.addfinalizer(wd.quit)
    wd.get(request.config.getoption("--url"))


@pytest.fixture(scope="session")
def opencart(request):
    return request.config.getoption("--address")
