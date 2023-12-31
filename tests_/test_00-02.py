from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.loginPage import LoginPage
from pages_.navigationBar import NavigationBar
from pages_.cartPage import CartPage

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")


loginPageObj = LoginPage(driver)
if loginPageObj._get_title() != "Amazon sign-In":
    print("Error: Wrong Page Title")
    exit(3)


loginPageObj.fill_username_field("lilmankan@gmail.com")
loginPageObj.validate_continue_button_text()
loginPageObj.click_to_continue_button()
loginPageObj.fill_password_field("amazonlilit2023@")
loginPageObj.click_to_signin_button()

navigationBarObj = NavigationBar(driver)
navigationBarObj.click_to_cart_button()


cartPageObj = CartPage(driver)
cartPageObj.delete_firstProduct_from_cart()


driver.close()