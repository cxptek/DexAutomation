from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base = BasePage(driver=driver)

    def enter_username(self, username):
        self.base.send_keys(locator="txtUsername", keys=username)

    def enter_password(self, password):
        self.base.send_keys(locator="txtPassword", keys=password)

    def click_login(self):
        self.base.click(locator="btnLogin")

    def homepage(self):
        self.base.wait_for_locator_visible(locator="txtDashboard")
        return self.base.selector(locator="txtDashboard").text