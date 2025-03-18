import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.logger import logger  # Import the logger


class BrowserUtils:
    """Utility class for browser setup and common actions."""

    COOKIE_NOTICE_BUTTON = (By.CSS_SELECTOR,
                            "button[data-a-target='consent-banner-accept']")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(text(),'Close')]")

    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        """Accept cookie notice if it appears."""
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.COOKIE_NOTICE_BUTTON)).click()
            logger.info("✅ Cookie notice accepted.")
        except:
            logger.info("ℹ️ No cookie notice found, continuing.")

    def handle_popups(self):
        """Close any pop-ups before loading the streamer page."""
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.CLOSE_MODAL_BUTTON)).click()
            logger.info("✅ Pop-up closed.")
        except:
            logger.info("ℹ️ No pop-ups found, continuing.")

    def take_screenshot(self, filename="twitch_test_screenshot.png"):
        # Ensure screenshots folder exists
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        """Take a screenshot and save it."""
        self.driver.save_screenshot(filename)
        logger.info(f"📸 Screenshot saved: {filename}")


@pytest.fixture
def setup_browser(request):
    """Fixture to initialize and return the browser driver with failure handling."""

    logger.info("🚀 Starting browser...")
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "Pixel 2"})

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver

    driver.quit()
    logger.info("🛑 Browser closed.")
