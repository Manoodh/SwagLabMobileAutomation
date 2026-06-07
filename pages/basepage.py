# Inside pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        """
        Accepts the active Appium remote driver execution context session
        """
        self.driver = driver
        # Standard explicit wait threshold engine (10 seconds maximum buffer)
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, locator: tuple):
        """Ensures an element is fully rendered and visible in the device viewport"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_mobile_element(self, locator: tuple):
        """Synchronizes and triggers a tap/click execution event on a target node"""
        element = self.wait_for_element(locator)
        element.click()

    def fill_mobile_field(self, locator: tuple, text: str):
        """Synchronizes, flushes, and types clear string input text into a mobile field"""
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_mobile_text(self, locator: tuple) -> str:
        """Extracts character metadata string text from an explicit target locator container"""
        element = self.wait_for_element(locator)
        return element.text