from features.helpers.driver import get_driver
from features.pages.base_page import find_element
import time


BOTAO_CANCELAR = "#cancel"
CARRINHO = ".shopping_cart_link"
BOTAO_CHECKOUT = "#checkout"
BTN_ADD_ITEM = '#add-to-cart-sauce-labs-backpack'
URL_CORRETA = "https://www.saucedemo.com/cart.html"



def ir_para_checkout():
    find_element(BTN_ADD_ITEM).click()
    find_element(CARRINHO).click()
    find_element(BOTAO_CHECKOUT).click()


def clicar_btn_cancelar():
    find_element(BOTAO_CANCELAR).click()

def esta_na_pagina_de_carrinho():
    url_atual = get_driver().current_url
    print(url_atual)
    assert URL_CORRETA == url_atual