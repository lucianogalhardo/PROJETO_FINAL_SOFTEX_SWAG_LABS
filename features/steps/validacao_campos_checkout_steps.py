from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.validacao_campos_checkout_page import *

@given(u'o usuário adiciona o produto "{produto}" ao carrinho para validação')
def adicionar_produto_checkout_page(context, produto):
    adicionar_produto_checkout()



@given(u'o usuário acessa o carrinho e clica em "Checkout"')
def acessar_checkout(context):
    ir_para_checkout()


@when(u'o usuário preenche apenas o primeiro nome e o CEP')
def preencher_parcial_checkout(context):
    preencher_parcial("David", "5300000")

@when(u'clica em "Continue"')
def clicar_continue(context):
    clicar_em_continue()



@then(u'deve ser exibida a mensagem de erro "{mensagem_erro}"')
def validar_erro_checkout(context, mensagem_erro):
    assert obter_erro_checkout() == mensagem_erro
