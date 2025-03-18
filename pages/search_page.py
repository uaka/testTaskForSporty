from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    """Page object for the search results page."""

    STREAMERS_LIST = (By.CSS_SELECTOR, "[role=list] a")

    def search_in_channels(self, to_search):
        self.driver.get("https://m.twitch.tv/search?term=" + to_search.replace(' ', "%20") + "&type=channels")

    def scroll_and_select_streamer(self):
        """Scroll down twice and click the first streamer."""
        self.scroll_down()
        self.scroll_down()
        streamers = self.driver.find_elements(*self.STREAMERS_LIST)
        if streamers:
            streamer_link = streamers[0].get_attribute("href")
            self.driver.get(streamer_link)
