import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self,driver):
        self.driver=driver


    def click(self,locator):
        self.driver.find_element(*locator).click()

    def send_keys(self,locator,text):
        self.driver.find_element(*locator).send_keys(text)

    def click_and_send_keys(self,locator,text):
        element = self.driver.find_element(*locator)
        element.click()
        element.send_keys(text)

    def wait_for_element(self,locator,timeout=10):
        wait = WebDriverWait(self.driver,timeout)
        wait.until(EC.visibility_of_element_located(locator))


    def is_element_displayed(self,locator):
        element = self.driver.find_element(*locator)
        return element.is_displayed()


    def swipe_up(self):
        size = self.driver.get_window_size()
        start_x = size['width'] /2
        start_y = size['height'] * .8
        end_y = size['height'] * .2
        self.driver.swipe(start_x,start_y,start_x,end_y,duration=800)
        time.sleep(1)


