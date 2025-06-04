from features.helpers.driver import get_driver
from features.pages.base_page import *
import time


# Mapeamento de elementos
BOTAO_ADD_CARRINHO = "add-to-cart-sauce-labs-backpack"
LINK_CARRINHO = "shopping_cart_link"
BOTAO_CHECKOUT = "checkout"
CAMPO_FIRST_NAME = "first-name"
CAMPO_LAST_NAME = "last-name"
CAMPO_ZIP_CODE = "postal-code"
BOTAO_CONTINUE = "continue"
BOTAO_FINISH = "finish"
CONTAINER_CONFIRMACAO = "checkout_complete_container"
BOTAO_BACK_HOME = "back-to-products"


def acessar_carrinho_com_um_item():
    
    # get_driver().get("https://www.saucedemo.com/inventory.html")
    # time.sleep(2)

    find_element_by_id(BOTAO_ADD_CARRINHO).click()
    time.sleep(1)
    
    find_element_by_class(LINK_CARRINHO).click()
    time.sleep(2)


def clicar_checkout():
    find_element_by_id(BOTAO_CHECKOUT).click()
    time.sleep(1)


def preencher_informacoes_usuario(first_name, last_name, zip_code):
    find_element_by_id(CAMPO_FIRST_NAME).send_keys(first_name)
    find_element_by_id(CAMPO_LAST_NAME).send_keys(last_name)
    find_element_by_id(CAMPO_ZIP_CODE).send_keys(zip_code)
    time.sleep(1)


def clicar_continue():
    find_element_by_id(BOTAO_CONTINUE).click()
    time.sleep(1)


def clicar_finish():
    find_element_by_id(BOTAO_FINISH).click()
    time.sleep(1)


def validar_mensagem_confirmacao():
    texto = find_element_by_id(CONTAINER_CONFIRMACAO).text
    assert "Thank you for your order!" in texto


def clicar_botao_back_home():
    find_element_by_id(BOTAO_BACK_HOME).click()
    time.sleep(2)


def validar_redirecionamento_para_inventario():
    url_atual = get_driver().current_url
    assert "inventory.html" in url_atual, f"URL inesperada: {url_atual}"
    time.sleep(2)
