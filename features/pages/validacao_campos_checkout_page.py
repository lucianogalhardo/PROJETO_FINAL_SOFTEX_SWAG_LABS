from features.helpers.driver import get_driver
from features.pages.base_page import find_element


PRODUTO = "#add-to-cart-sauce-labs-bolt-t-shirt"
CARRINHO = ".shopping_cart_link"
BOTAO_CHECKOUT = "#checkout"
CAMPO_FIRST_NAME = "#first-name"
CAMPO_POSTAL_CODE = "#postal-code"
BOTAO_CONTINUE = "#continue"
TEXTO_MENSAGEM_ERROR = "h3[data-test='error']"


def adicionar_produto_checkout():
    find_element(PRODUTO).click()

def ir_para_checkout():
    find_element(CARRINHO).click()
    find_element(BOTAO_CHECKOUT).click()

def preencher_parcial(first, zip_code):
    find_element(CAMPO_FIRST_NAME).send_keys("David")
    find_element(CAMPO_POSTAL_CODE).send_keys("5300000")

def clicar_em_continue():
    find_element(BOTAO_CONTINUE).click()

def obter_erro_checkout():
    return find_element(TEXTO_MENSAGEM_ERROR).text