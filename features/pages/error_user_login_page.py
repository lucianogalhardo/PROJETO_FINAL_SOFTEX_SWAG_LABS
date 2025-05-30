from features.helpers.driver import get_driver
from features.pages.base_page import find_element

CAMPO_NOME = "#user-name"
CAMPO_SENHA = "#password"
BOTAO_LOGIN = "#login-button"

def acessar_pagina_login():
    get_driver().get("https://www.saucedemo.com/")

def realizar_login(usuario, senha):
    find_element(CAMPO_NOME).send_keys(usuario)
    find_element(CAMPO_SENHA).send_keys(senha)
    find_element(BOTAO_LOGIN).click()
