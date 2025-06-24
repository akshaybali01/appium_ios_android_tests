import os.path

import pytest
import json

from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver

from drivers.appium_driver import create_driver

def pytest_addoption(parser):
    parser.addoption("--platform", default="android")


@pytest.fixture(scope="function")
def driver(request):
    driver = create_driver(request)
    yield driver
    driver.quit()



