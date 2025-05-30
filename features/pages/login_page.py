from features.pages.base_page import *
from features.helpers.driver import get_driver

CAMPO_USUARIO = "#user-name"
CAMPO_SENHA = "#password"
BOTAO_LOGIN = "#login-button"
MENSAGEM_ERRO = "h3[data-test='error']"

def abrir_pagina_login():
    get_driver().get("https://www.saucedemo.com/")

def preencher_usuario(usuario):
    wait_for_element(CAMPO_USUARIO) 
    find_element(CAMPO_USUARIO).clear()
    find_element(CAMPO_USUARIO).send_keys(usuario)

def preencher_senha(senha="secret_sauce"):
    wait_for_element(CAMPO_SENHA)
    find_element(CAMPO_SENHA).clear()
    find_element(CAMPO_SENHA).send_keys(senha)

def clicar_botao_login():
    wait_for_element(BOTAO_LOGIN)
    find_element(BOTAO_LOGIN).click()

def buscar_mensagem_erro():
    wait_for_element(MENSAGEM_ERRO)
    return find_element(MENSAGEM_ERRO).text

def esta_na_pagina_login():
    url = get_driver().current_url
    return "saucedemo.com" in url and "inventory" not in url

def login_usuario(usuario, senha="secret_sauce"):
    abrir_pagina_login()
    preencher_usuario(usuario)
    preencher_senha(senha)
    clicar_botao_login()
