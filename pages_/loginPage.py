from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
class LoginPage():

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        pass

    def fill_username_field(self, username):
        userNameFieldElement = self.driver.find_element(By.ID, "ap_email")
        userNameFieldElement.clear()
        userNameFieldElement.send_keys(username)


    def click_to_continue_button(self):
        continueButtonElement = self.driver.find_element(By.ID, "continue")
        continueButtonElement.click()

    def fill_password_field(self, password):
        passwordFieldElement = self.driver.find_element(By.ID, "ap_password")
        passwordFieldElement.clear()
        passwordFieldElement.send_keys(password)

    def click_to_signin_button(self):
        sleep(6)
        signInButtonElement = self.driver.find_element(By.ID, "signInSubmit")
        signInButtonElement.click()
        sleep(6)