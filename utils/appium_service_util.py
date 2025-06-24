from appium.webdriver.appium_service import AppiumService

appium_service=AppiumService()
def start_appium():
    if not appium_service.is_running:
        appium_service.start(args=["--port","4723"])

def stop_appium():
    if appium_service.is_running:
        appium_service.stop()




