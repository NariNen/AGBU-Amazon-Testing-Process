from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._cartButtonLocator = (By.ID, "nav-cart-count-container")
        self._searchButtonLocator = (By.ID, "twotabsearchtextbox")
        self._amazonButtonLocator = (By.ID, "nav-logo-sprites")
        self._allSearchButtonLocator = (By.ID, "searchDropdownBox")
    def click_to_cart_button(self):
        cartButtonElement = self.driver.find_element(self._cartButtonLocator)
        self._click(cartButtonElement)
    def search_on_cart_button(self):
        searchButtonElement = self.driver.find_element(self._searchButtonLocator)
        self._click(searchButtonElement)
    def click_to_amazon_button_locator(self):
        amazonButtonLocator = self.driver.find_element(self._amazonButtonLocator)
        self._click(amazonButtonLocator)
    def click_all_search_button_locator(self):
        allSearchButtonLocator = self.driver.find_element(self._allSearchButtonLocator)
        self._click(allSearchButtonLocator)
