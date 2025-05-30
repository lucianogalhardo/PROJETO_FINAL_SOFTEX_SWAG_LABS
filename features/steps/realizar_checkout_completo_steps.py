from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.realizar_checkout_completo_page import *


@given(u'o usuário adiciona o produto "{produto}" ao carrinho')
def adicionar_produto(context, produto):
    adicionar_ao_carrinho(produto)


@when(u'o usuário acessa o carrinho e clica em "Checkout"')
def acessar_checkout(context):
    ir_para_checkout()


@when(u'o usuário preenche os campos Nome, Sobrenome e CEP')
def preencher_checkout_info(context):
    preencher_info_pessoal("Janielson", "Anjos", "53330740")


@when(u'o usuário clica em "Continue" e depois em "Finish"')
def finalizar_pedido(context):
    finalizar_checkout()


@then(u'a mensagem "{mensagem_correta}" deve ser exibida')
def verificar_mensagem_final(context, mensagem_correta):
    assert verificar_mensagem_sucesso() == mensagem_correta
