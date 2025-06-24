from pages.base_page import BasePage
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class LoginPage(BasePage):
    USERNAME_FIELD= (AppiumBy.ACCESSIBILITY_ID, "test-Username")
    PASSWORD_FIELD= (AppiumBy.ACCESSIBILITY_ID, "test-Password")
    LOGIN_BUTTON= (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")

    def login(self,username,password):
        self.wait_for_element(self.USERNAME_FIELD,20)
        self.click_and_send_keys(self.USERNAME_FIELD,username)
        self.click_and_send_keys(self.PASSWORD_FIELD,password)
        self.click(self.LOGIN_BUTTON)

