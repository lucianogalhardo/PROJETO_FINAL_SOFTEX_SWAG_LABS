from features.helpers.driver import get_driver
from features.pages.base_page import *
import time


# Mapeamento de elementos
CONTINUE_SHOPPING_BUTTON = "continue-shopping"

def acessar_carrinho():
    get_driver().get("https://www.saucedemo.com/cart.html")
    time.sleep(1)


def clicar_continue_shopping():
    find_element_by_id("continue-shopping").click()
    time.sleep(1)


def validar_pagina_inventario():
    url_atual = get_driver().current_url
    assert "inventory.html" in url_atual, f"Redirecionamento errado: {url_atual}"
