from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class StreamerPage(BasePage):
    """Page object for the streamer's profile page."""

    FOLLOW_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Follow ']")

    def is_page_opened(self):
         return  self.is_element_displayed(self.FOLLOW_BUTTON)
