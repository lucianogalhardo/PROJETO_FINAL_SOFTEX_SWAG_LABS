import os
from features.helpers.driver import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from behave.model_core import Status

# HOOKS
def before_scenario(context, scenario):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    set_driver(driver)
    context.driver = driver

def after_scenario(context, scenario):
    print(scenario.name)
    driver = get_driver()

    if scenario.status == Status.failed:
        screenshor_dir = "screenshots"
        os.makedirs(screenshor_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshor_dir, f"{scenario.name.replace(' ', '_')}.png")
        driver.save_screenshot(screenshot_path)

    driver.quit()