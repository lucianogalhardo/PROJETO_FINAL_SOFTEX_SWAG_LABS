from features.helpers.driver import get_driver
from features.pages.base_page import find_element_by_id
from selenium.webdriver.support.ui import Select
import time

# Mapeamento de elementos
URL_LOGIN = "https://www.saucedemo.com/"
CAMPO_USERNAME = "user-name"
CAMPO_PASSWORD = "password"
BOTAO_LOGIN = "login-button"


def acessar_page():
    get_driver().get("https://www.saucedemo.com/")
    time.sleep(2)

def inserir_credenciais(username, password):
    find_element_by_id("user-name").send_keys(username)
    find_element_by_id("password").send_keys(password)
    time.sleep(1)

def clicar_botao_login():
    find_element_by_id("login-button").click()
    time.sleep(2)

def validar_pagina_inventario():
    url_atual = get_driver().current_url
    assert "inventory" in url_atual, f"URL incorreta após login: {url_atual}"

def realizar_login(username, password):
    acessar_page()
    inserir_credenciais(username, password)
    clicar_botao_login()
