from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common_.utilities_.customLogger import *

class BasePage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
    def _find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
            logger("INFO", f"The locator of element is found successfully: {locator}")
            return element

        except:
            print("Error: Element Not Found")
            logger("ERROR", "Element Not Found")
            exit(1)
    def _click(self, webElement):
        webElement.click()
        logger("INFO", "The element is clicked.")
    def _fill_field(self, webElement, text):
        webElement.clear()
        webElement.send_keys(text)
        logger("INFO", "Text has been added to the element")
    def _get_title(self):
        logger("INFO", f"Title successfully found: {self.driver.title}")
        return self.driver.title
    def _get_text(self, element):
        logger("INFO", f"Text is founded: {element.text}")
        return element.text







