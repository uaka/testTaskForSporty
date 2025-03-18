import pytest
from pages.search_page import SearchPage
from pages.streamer_page import StreamerPage
from utils.browser_setup import setup_browser, BrowserUtils
from utils.logger import logger

TO_SEARCH = "StarCraft II"


def test_twitch_search(setup_browser, request):
    """Test Twitch search and streamer selection."""
    driver = setup_browser
    browser_utils = BrowserUtils(driver)
    try:
        search_page = SearchPage(driver)
        logger.info("🔎 Searching for 'StarCraft II'...")
        search_page.search_in_channels(TO_SEARCH)
        browser_utils.accept_cookies()

        logger.info("📜 Scrolling and selecting a streamer...")

        search_page.scroll_and_select_streamer()

        logger.info("🛠 Handling pop-ups (if any)...")
        browser_utils.handle_popups()

        logger.info("📸 Taking a screenshot...")
        browser_utils.take_screenshot()

        streamer_page = StreamerPage(driver)
        assert streamer_page.is_page_opened()  # Mark test as passed if everything runs correctly
        logger.info("✅ Test completed successfully.")

    except Exception as e:
        # Capture failure screenshot
        screenshot_path = f"screenshots/{request.node.name}_failed.png"
        browser_utils.take_screenshot(screenshot_path)
        logger.error(f"❌ Test failed! Screenshot saved: {screenshot_path}")

        pytest.fail(f"Test failed due to: {e}")  # Mark test as failed
