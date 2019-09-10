"""this is a main page tests file"""
import pytest


@pytest.fixture(scope="session")
def main_page(request, driver):
    """will use this later"""
    return driver.get(request.config.getoption("--address"))


def test_open_main_page(request, driver):
    """test to open a site and to check if its the site we needed"""
    url = request.config.getoption("--address")
    driver.get(url)
    assert "opencart" in driver.current_url
    # or another assert inbefore we used PageObject"""
    assert driver.find_element_by_xpath("/html/body/header/div/div/div[1]/div/h1/a")
