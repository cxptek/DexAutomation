from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.readJS import readJS
import logging

# logging.basicConfig(level=logging.DEBUG)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = readJS('data/locator.json')
    
    def selector(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.locators[locator]))
            )
            return element
        except:
            print(f'Locator {locator} not found')
            return None
            
    def wait_for_locator_visible(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.locators[locator])))
        except:
            print(f'Locator {locator} not found')

    def click(self, locator):
        el = self.selector(locator)
        if el:
            el.click()
        else:
            print(f'Locator {locator} is not clickable')

    def send_keys(self, locator, keys):
        el = self.selector(locator)
        if el:
            el.send_keys(keys)
        else:
            print(f'Locator {locator} is not sendable')
    
    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        print(f'Screenshot saved as {filename}')