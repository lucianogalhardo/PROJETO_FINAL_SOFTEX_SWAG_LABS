from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select


CARRINHO = ".shopping_cart_link"
BOTAO_CHECKOUT = "#checkout"
CAMPO_FIRST_NAME = "#first-name"
CAMPO_LAST_NAME = "#last-name"
CAMPO_POSTAL_CODE = "#postal-code"
BOTAO_CONTINUE = "#continue"
BOTAO_FINISH = "#finish"
TEXTO_MENSAGEM_ERROR = ".complete-header"
BTN_ADD_ITEM = '#add-to-cart-sauce-labs-backpack'


def adicionar_ao_carrinho(produto):
    find_element(BTN_ADD_ITEM).click()

def ir_para_checkout():
    find_element(CARRINHO).click()
    find_element(BOTAO_CHECKOUT).click()

def preencher_info_pessoal(first, last, zip_code):
    find_element(CAMPO_FIRST_NAME).send_keys(first)
    find_element(CAMPO_LAST_NAME).send_keys(last)
    find_element(CAMPO_POSTAL_CODE).send_keys(zip_code)

def finalizar_checkout():
    find_element(BOTAO_CONTINUE).click()
    find_element(BOTAO_FINISH).click()

def verificar_mensagem_sucesso():
    return find_element(TEXTO_MENSAGEM_ERROR).text