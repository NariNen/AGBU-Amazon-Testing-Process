from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class productSearching(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._searchAmazonButton = (By.ID, "twotabsearchtextbox")
        self._searchingButton = (By.ID, "nav-search-submit-button")
        self._priceLocator = (By.XPATH, "//span[@id='p_36/2661613011']/span/a/span")
    def click_to_search_amazon_button(self):
        searchAmazonButton = self._find_element(self._searchAmazonButton)
        self._fill_field(searchAmazonButton)
    def searching_button(self):
        searchingButton = self._find_element(self._searchingButton)
        self._click(searchingButton)
    def price_locator(self):
        priceLocator = self._find_element(self._priceLocator)
        self._click(priceLocator)
