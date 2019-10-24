from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def test_drag_and_drop():
    """use ActionChains click_and_hold fot a simple dragndrop test"""
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://marcojakob.github.io/dart-dnd/basic/")
    document = driver.find_elements_by_css_selector(
        "div[class='container'] img")
    trash = driver.find_element_by_class_name("trash")
    for doc in document:
        ActionChains(driver).pause(0.5).move_to_element(doc).\
            click_and_hold().move_to_element(
            trash).release().perform()

    driver.quit()
