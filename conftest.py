import os.path

import pytest
import json

from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver

from drivers.appium_driver import create_driver
from utils.appium_service_util import start_appium, stop_appium


@pytest.fixture(scope="session",autouse=True)
def appium_server():
    start_appium()
    print("appium server started...")
    yield
    stop_appium()


def pytest_addoption(parser):
    parser.addoption("--platform", default="android")


@pytest.fixture(scope="function")
def driver(request):
    driver = create_driver(request)
    yield driver
    driver.quit()



