import pytest
import sys

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://127.0.0.1/opencart/", help="Opencard address")
    parser.addoption("--browser", action="store", default="firefox", help="Browser name")


@pytest.fixture(params=["chrome", "firefox"])
@pytest.fixture(scope="session", autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("start-maximized")
        options.add_argument("--headless")
        profile = webdriver.FirefoxProfile()
        profile.set_preference('app.update.auto', False)
        profile.set_preference('app.update.enabled', False)
        profile.accept_untrusted_certs = True
        wd = webdriver.Firefox(firefox_options=options)

    elif browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("--headless")
        wd = webdriver.Chrome(chrome_options=options)

    else:
        print("Internet Explorer is a crap!")
        wd = webdriver.Ie(executable_path="\\home\\grace\\PycharmProjects\\otus_qa\\IEDriverServer.exe")
        wd.quit()
        sys.exit(1)
    yield wd
    request.addfinalizer(wd.quit)


@pytest.fixture(scope="session")
def opencart(request):
    return request.config.getoption("--address")
