from features.pages.base_page import *
from features.helpers.driver import get_driver
import time


BOTAO_ADD = "#add-to-cart-sauce-labs-backpack"
BOTAO_REMOVE = "#remove-sauce-labs-backpack"
ITEM_INVENTARIO = ".inventory_item_name"
PAGINA_CARRINHO = ".shopping_cart_link"
PAGINA_INVENTARIO = "#inventory_container"
ICONE_CARRINHO = "#shopping_cart_container > a > span"
BOTAO_CONTINUAR_COMPRANDO = "#continue-shopping"



# ADICIONANDO O ITEM AO CARRINHO
def adicionar_item_ao_carrinho():
    find_element(BOTAO_ADD).click()

# VERIFICANDO SE O ITEM ESTÁ NO CARRINHO
def verificar_item_no_carrinho():
    find_element(PAGINA_CARRINHO).click()
    assert get_element_text(ITEM_INVENTARIO) == "Sauce Labs Backpack", "O item não está no carrinho."

# removendo o item do carrinho
def remover_item_do_carrinho():
    find_element(BOTAO_CONTINUAR_COMPRANDO).click()
    find_element(BOTAO_REMOVE).click()

# VERIFICANDO SE O ITEM FOI REMOVIDO DO CARRINHO
def verificar_item_removido():
    find_element(PAGINA_CARRINHO).click()
    assert not get_element_text(ITEM_INVENTARIO) == "Sauce Labs Backpack", "O item ainda está no carrinho."

# VERIFICANDO SE O USUÁRIO ESTÁ NA PÁGINA DE INVENTÁRIO
def pagina_inventario():
    find_element(PAGINA_INVENTARIO).click()
    
    url_atual = get_driver().current_url
    assert "inventory.html" in url_atual, "O usuário não está na página de inventário."
    