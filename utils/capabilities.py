
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  time
import json
def load_config():
    with open("config/ios.json") as file:
        return json.load(file)

def create_ios_driver():
    data = load_config()
    print(data)

    desired_capabilities = load_config()
    options = XCUITestOptions().load_capabilities(desired_capabilities)
    driver = webdriver.Remote("http://127.0.0.1:4723",options=options)
    return driver




