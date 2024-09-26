import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the WebDriver (Chrome in this case)
        cls.driver = webdriver.Chrome()

    def test_search_can_tim(self):
        # Go to Google
        self.driver.get("https://admin-uat.25fit.com")

        # Find the search box using the name attribute
        search_box = self.driver.find_element(By.NAME, "username")

        # Enter the search query "can tim"
        search_box.send_keys("can tim")

    @classmethod
    def tearDownClass(cls):
        # Optionally close the browser after all tests are done
        cls.driver.quit()

# Run the tests
if __name__ == "__main__":
    unittest.main()
