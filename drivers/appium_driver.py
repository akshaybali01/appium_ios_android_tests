import os.path
import json
from appium import  webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


# load config file
def load_config(platform):
    file_path=f"config/{platform}.json"
    if not  os.path.exists(file_path):
        raise FileNotFoundError(f"Configration file not found, {file_path}")

    with open(file_path) as file:
        return json.load(file)

def create_driver(request):
    platform = request.config.getoption("--platform")
    desired_capabilities = load_config(platform)
    if platform=='android':
        options =UiAutomator2Options().load_capabilities(desired_capabilities)
    elif platform=='ios':
        options=XCUITestOptions().load_capabilities(desired_capabilities)

    driver = webdriver.Remote("http://127.0.0.1:4723",options=options)
    return driver


