from features.helpers.driver import get_driver
from features.pages.base_page import *
from features.pages import login_page

URL_LOGIN = "https://www.saucedemo.com/"
BOTAO_ADD_ITEM = "#add-to-cart-sauce-labs-backpack"
ICON_CARRINHO = ".shopping_cart_link"
BOTAO_CHECKOUT = "#checkout"
CAMPO_FIRST_NAME = "#first-name"
CAMPO_LAST_NAME = "#last-name"
CAMPO_POSTAL = "#postal-code"
BOTAO_CONTINUE = "#continue"
BOTAO_FINISH = "#finish"
MENSAGEM_SUCESSO = ".complete-header"


def login_usuario_standard_user(usuario, senha="secret_sauce"):
    login_page.abrir_pagina_login()
    login_page.preencher_usuario(usuario)
    login_page.preencher_senha(senha)
    login_page.clicar_botao_login()

def adicionar_item_ao_carrinho():
    wait_for_element(BOTAO_ADD_ITEM)
    find_element(BOTAO_ADD_ITEM).click()

def ir_para_checkout():
    find_element(ICON_CARRINHO).click()
    wait_for_element(BOTAO_CHECKOUT)
    find_element(BOTAO_CHECKOUT).click()

def preencher_checkout(nome, sobrenome, cep):
    wait_for_element(CAMPO_FIRST_NAME)
    find_element(CAMPO_FIRST_NAME).send_keys(nome)
    find_element(CAMPO_LAST_NAME).send_keys(sobrenome)
    find_element(CAMPO_POSTAL).send_keys(cep)
    find_element(BOTAO_CONTINUE).click()

def finalizar_compra():
    wait_for_element(BOTAO_FINISH)
    find_element(BOTAO_FINISH).click()

def mensagem_sucesso_exibida():
    wait_for_element(MENSAGEM_SUCESSO)
    return get_element_text(MENSAGEM_SUCESSO)
