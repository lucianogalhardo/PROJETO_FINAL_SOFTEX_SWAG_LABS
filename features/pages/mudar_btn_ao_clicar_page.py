from features.helpers.driver import get_driver
from features.pages.base_page import find_element



BOTAO_ADD_CART = "#add-to-cart-sauce-labs-onesie"
BOTAO_REMOVE_CART = "#remove-sauce-labs-onesie"


def adicionar_sauce_labs_onesie():
    find_element(BOTAO_ADD_CART).click()

def verificar_botao_mudou():
    return find_element(BOTAO_REMOVE_CART).text