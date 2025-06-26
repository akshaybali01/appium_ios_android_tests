import os.path

import pytest
from _pytest.reports import TestReport
from pytest_html import extras  # Make sure pytest-html is installed
from drivers.appium_driver import create_driver
from utils.appium_service_util import start_appium, stop_appium
from datetime import datetime


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

# # Pytest hook to add screenshots to HTML report on failure
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report: TestReport = outcome.get_result()
#
#     if report.when == "call" and report.failed:
#         driver = item.funcargs.get("driver")
#         if driver:
#             screenshots_dir = "screenshots"
#             os.makedirs(screenshots_dir, exist_ok=True)
#
#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#             file_name = f"{item.name}_{timestamp}.png"
#             screenshot_path = os.path.join(screenshots_dir, file_name)
#
#             driver.save_screenshot(screenshot_path)
#
#             # Embed screenshot in HTML report
#             extra = getattr(report, "extra", [])
#             if os.path.exists(screenshot_path):
#                 relative_path = os.path.relpath(screenshot_path, start="reports")
#                 html = f'<div><img src="{relative_path}" alt="screenshot" style="width:300px;height:auto;" onclick="window.open(this.src)" /></div>'
#                 extra.append(extras.html(html))
#             report.extra = extra



import os
from datetime import datetime
import pytest
from pytest_html import extras
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshots_dir, file_name)

            # Save screenshot
            driver.save_screenshot(screenshot_path)

            # Attach screenshot to HTML report
            extra = getattr(report, "extra", [])
            if os.path.exists(screenshot_path):
                relative_path = os.path.relpath(screenshot_path, start="reports")
                html = f'<div><img src="{relative_path}" alt="screenshot" style="width:300px;height:auto;" onclick="window.open(this.src)" /></div>'
                extra.append(extras.html(html))
            report.extra = extra

            # 🔥 Attach screenshot to Allure report
            if os.path.exists(screenshot_path):
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name=f"screenshot_{timestamp}",
                        attachment_type=allure.attachment_type.PNG
                    )




