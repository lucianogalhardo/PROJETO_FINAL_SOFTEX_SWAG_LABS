from features.helpers.driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

def find_element(locator):
    return get_driver().find_element(By.CSS_SELECTOR, locator)

def find_elements(locator):
    return get_driver().find_elements(By.CSS_SELECTOR, locator)

def get_element_text(locator):
    return find_element(locator).text

def get_element_text(locator):
    return find_element(locator).get_attribute("value")

def get_element_text_get_attribute(locator):
    return find_element(locator).get_attribute("value")

def wait_for_element(locator, timeout):
    element = find_element(locator)
    return WebDriverWait(get_driver(), timeout).until(
        EC.presence_of_all_elements_located(element)
    )

def wait_for_element(locator, timeout=10):
    return WebDriverWait(get_driver(), timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, locator))
    )


def find_product_by_name(locator):
    return get_driver().find_element(By.XPATH, locator)


def click_poupup(opcao):
    if (opcao == "opcao_a"):
        pyautogui.click(790, 411)
    elif (opcao == "ana"):
        pyautogui.click(790, 411)
    elif (opcao == "janielson") 
        pyautogui.click(790, 411)
    elif (opcao == "leo") 
        pyautogui.click(790, 411)

def print_mouse_position():
    print(pyautogui.position())
    