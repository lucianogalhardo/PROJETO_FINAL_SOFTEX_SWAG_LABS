
from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select
import time



# Mapeamento de campos para interação
MENU_LATERAL = "#react-burger-menu-btn"
OPCAO_RESET_APP_STATE = "#reset_sidebar_link"
BOTAO_ADD = "#add-to-cart-sauce-labs-backpack"
BOTAO_REMOVE = "#remove-sauce-labs-backpack"

# Variáveis globais


# Encapsulamento das ações de interação com a página
def clicar_opcao_reset():
    find_element(MENU_LATERAL).click()
    time.sleep(2)  # Espera para evitar problemas de sincronização
    find_element(OPCAO_RESET_APP_STATE).click()
    time.sleep(2)  # Espera para evitar problemas de sincronização


# ADICIONANDO O ITEM AO CARRINHO
def adicionar_item_ao_carrinho():
    find_element(BOTAO_ADD).click()

# Verificar texto botao
def verificar_status_butao_add():
    return find_element(BOTAO_ADD).text
    
def verificar_status_butao_remove():
    return find_element(BOTAO_REMOVE).text

