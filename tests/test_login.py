import sys
import os
import unittest 
from selenium import webdriver

from utils.config import BASE_URL
from pages.login_page import LoginPage
from utils.readJS import readJS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(sys.path)
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        self.login_page = LoginPage(self.driver)
        
    def test_login(self, data=readJS('data/data.json')['login']): 
        self.login_page.click_login_header()
        self.login_page.enter_email(data['email'])
        self.login_page.enter_password(data['password'])
        self.login_page.click_login()

        price_text = self.login_page.homepage()
        print (price_text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()