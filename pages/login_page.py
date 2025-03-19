from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base = BasePage(driver=driver)

    def click_login_header(self):
        self.base.click(locator="btnLoginHeader")

    def enter_email(self, email):
        self.base.send_keys(locator="txtEmail", keys=email)

    def enter_password(self, password):
        self.base.send_keys(locator="txtPassword", keys=password)

    def click_login(self):
        self.base.click(locator="btnLogin")

    def homepage(self):
        # self.base.wait_for_locator_visible(locator="txtPrice")
        element = self.base.selector(locator="txtPrice")
        if element is not None:
            return element.text
        else:
            raise AttributeError("Element with locator 'txtPrice' not found or is None")