from features.helpers.driver import get_driver
from features.pages.base_page import *
import time


# Mapeamento de elementos
URL_CARRINHO = "https://www.saucedemo.com/cart.html"
BOTAO_CHECKOUT = "checkout"
CAMPO_FIRST_NAME = "first-name"
CAMPO_LAST_NAME = "last-name"
CAMPO_ZIP_CODE = "postal-code"
BOTAO_CONTINUE = "continue"
BOTAO_FINISH = "finish"
CONTAINER_CONFIRMACAO = "checkout_complete_container"


def acessar_carrinho():
    get_driver().get("https://www.saucedemo.com/cart.html")
    time.sleep(2)

def clicar_checkout():
    find_element_by_id("checkout").click()
    time.sleep(2)

def preencher_informacoes_usuario(first_name, last_name, zip_code):
    find_element_by_id("first-name").send_keys(first_name)
    find_element_by_id("last-name").send_keys(last_name)
    find_element_by_id("postal-code").send_keys(zip_code)
    time.sleep(3)

def clicar_continue():
    find_element_by_id("continue").click()
    time.sleep(2)

def clicar_finish():
    find_element_by_id("finish").click()
    time.sleep(2)

def validar_mensagem_confirmacao():
    texto = find_element_by_id("checkout_complete_container").text
    assert "Thank you for your order!" in texto
