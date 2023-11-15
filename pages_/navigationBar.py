from selenium.webdriver.common.by import By
from pages_.basePage import BasePage
class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._cartButtonLocator = (By.ID, "nav-cart-count-container")
        self._searchFiledLocator = (By.CLASS_NAME, "nav-input nav-progressive-attribute")
        self._searchingButtonLocator = (By.ID, "nav-search-submit-button")
        self._amazonButtonLocator = (By.ID, "nav-logo-sprites")
        self._allSearchButtonLocator = (By.ID, "searchDropdownBox")
    def click_to_cart_button(self):
        cartButtonElement = self.driver.find_element(self._cartButtonLocator)
        self._click(cartButtonElement)
    def search_field_element(self):
        searchFieldElement = self._fill_field(self._searchFiledLocator)
        self._fill_field(searchFieldElement, "product")

    def searching_button_element(self):
        searchingButtonElement = self._find_element(self._searchingButtonLocator)
        self._click(searchingButtonElement)
    def click_to_amazon_button_locator(self):
        amazonButtonLocator = self.driver.find_element(self._amazonButtonLocator)
        self._click(amazonButtonLocator)
    def click_all_search_button_locator(self):
        allSearchButtonLocator = self.driver.find_element(self._allSearchButtonLocator)
        self._click(allSearchButtonLocator)
