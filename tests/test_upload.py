import pytest

from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("catalog_page")
@pytest.mark.usefixtures("login")
def test_upload_file(catalog_page, driver):
    """test for uploading a file"""
    catalog_page.open_catalog()
    catalog_page.open_downloads_page()
    catalog_page.click_add_new()
    catalog_page.click_upload_button()
    catalog_page.send_filename("/home/grace/Downloads/pic.jpg")
    ActionChains(driver).perform()
    catalog_page.accept_alert()
    catalog_page.set_download_name("downloadname")
    catalog_page.set_mask("mask")
    catalog_page.click_save_changes()
    alert = catalog_page.find_alert()
    assert alert.text == "Success: You have modified downloads!\n×"
