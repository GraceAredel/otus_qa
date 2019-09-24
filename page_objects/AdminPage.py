from locators.AdminLogin import AdminLoginPageLocators


class AdminPage:
    """base class for methods on login page"""
    def __init__(self, driver):
        self.driver = driver

    def login(self, login, password):
        self.driver.find_element(*AdminLoginPageLocators.USERNAME).send_keys(login)
        self.driver.find_element(*AdminLoginPageLocators.PASSWORD).send_keys(password)
        self.driver.find_element(*AdminLoginPageLocators.BUTTON).click()

    def reset_password(self, email):
        self.driver.find_element(*AdminLoginPageLocators.FORGOTTEN_PASSWORD).click()
        self.driver.find_element(*AdminLoginPageLocators.EMAIL).send_keys(email)
