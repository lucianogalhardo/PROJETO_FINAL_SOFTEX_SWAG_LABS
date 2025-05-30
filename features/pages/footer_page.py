from features.helpers.driver import get_driver
from selenium.webdriver.common.by import By
import time


def clicar_icones_footer():
    driver = get_driver()
    links = {}

    
    janela_principal = driver.current_window_handle

    
    driver.find_element(By.CLASS_NAME, "social_twitter").click()
    time.sleep(2)
    for janela in driver.window_handles:
        if janela != janela_principal:
            driver.switch_to.window(janela)
            time.sleep(2)
            links["Twitter"] = driver.current_url
            driver.close()
            driver.switch_to.window(janela_principal)
            break
    time.sleep(3)

    driver.find_element(By.CLASS_NAME, "social_facebook").click()
    time.sleep(2)
    for janela in driver.window_handles:
        if janela != janela_principal:
            driver.switch_to.window(janela)
            links["Facebook"] = driver.current_url
            driver.close()
            driver.switch_to.window(janela_principal)
            break
    time.sleep(3)

    
    driver.find_element(By.CLASS_NAME, "social_linkedin").click()
    time.sleep(3)
    for janela in driver.window_handles:
        if janela != janela_principal:
            driver.switch_to.window(janela)
            links["Linkedin"] = driver.current_url
            driver.close()
            driver.switch_to.window(janela_principal)
            break

    return links