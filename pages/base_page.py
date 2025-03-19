from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.readJS import readJS
import logging

logging.basicConfig(level=logging.INFO)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = readJS('data/locator.json')
    
    def selector(self, locator, timeout=15):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, self.locators[locator]))
            )
            return element
        except Exception as e:
            logging.error(f'Locator {locator} not found within {timeout} seconds. Exception: {e}')
            return None

    # def wait_for_locator_visible(self, locator, timeout=15):
    #     try:
    #         WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, self.locators[locator])))
    #     except Exception as e:
    #         logging.error(f'Locator {locator} not found within {timeout} seconds. Exception: {e}')

    def click(self, locator, timeout=15):
        el = self.selector(locator, timeout)
        if el:
            el.click()
        else:
            logging.error(f'Locator {locator} is not clickable')

    def send_keys(self, locator, keys, timeout=15):
        el = self.selector(locator, timeout)
        if el:
            el.send_keys(keys)
        else:
            logging.error(f'Locator {locator} is not sendable')
    
    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        logging.info(f'Screenshot saved as {filename}')