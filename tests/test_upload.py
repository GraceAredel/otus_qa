import logging
import time
import pytest


@pytest.mark.usefixtures("logger")
@pytest.mark.usefixtures("catalog_page")
@pytest.mark.usefixtures("login")
def test_upload_file(catalog_page, driver, logger):
    """test for uploading a file"""
    logger = logging.getLogger("otus_qa")
    catalog_page.open_catalog()
    catalog_page.open_downloads_page()
    catalog_page.click_add_new()
    catalog_page.click_upload_button()
    try:
        time.sleep(5)
        catalog_page.send_filename("/home/grace/Downloads/pic.jpg")
        logger.info("trying to upload the file")
    except Exception as e:
        logger.error(f"Unable to upload a file, reason: {e}")
        catalog_page.upload_file_script("/home/grace/Downloads/pic.jpg")
    catalog_page.accept_alert()
    catalog_page.set_download_name("downloadname")
    catalog_page.set_mask("mask")
    catalog_page.click_save_changes()
    alert = catalog_page.find_alert()
    assert alert.text == "Success: You have modified downloads!\n×"
