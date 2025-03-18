from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    """Base class for all pages, containing common Selenium actions."""

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator):
        """Wait for element to be clickable and click it."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        """Find an input field and enter text."""
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def wait_for_element(self, locator):
        """Wait until an element appears."""
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))


    def is_element_displayed(self, locator):
        """
        Check if an element is visible on the page.

        :param locator: Tuple (By strategy, locator string)
        :return: True if element is visible, False otherwise
        """
        try:
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False  # Return False if element is not found or not visible

    def scroll_down(self):
        """Scroll down the page."""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
