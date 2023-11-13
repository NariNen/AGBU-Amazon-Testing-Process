from selenium.webdriver.common.by import By
from pages_.basePage import BasePage


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._cartButtonLocator = (By.ID, "nav-cart-count-container")

    def click_to_cart_button(self):
        cartButtonElement = self.driver.find_element(self._cartButtonLocator)
        self._click(cartButtonElement)

