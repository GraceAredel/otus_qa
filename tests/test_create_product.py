import pytest


@pytest.mark.usefixtures("catalog_page")
@pytest.mark.usefixtures("login")
def test_upload_file(catalog_page):
    catalog_page.open_catalog()
    catalog_page.open_downloads_page()

