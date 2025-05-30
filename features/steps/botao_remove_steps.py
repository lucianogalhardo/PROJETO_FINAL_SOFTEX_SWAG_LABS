import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.base_page import *
from features.pages.botao_remove_page import *


@given(u'que o usuário adicionou o produto "Sauce Labs BackPack" clicando no botão "Add to cart"')
def adicionar_item(context):
    adicionar_item_ao_carrinho()
    time.sleep(2)


@when(u'o usuário acessar a página do carrinho clicar no botão "Remove" do produto "Sauce Labs BackPack"')
def remover_item(context):
    verificar_item_no_carrinho()
    time.sleep(5)
    #remover_item_do_carrinho()

@then(u'o produto escolhido será removido do carrinho')
def item_removido(context):
    remover_item_do_carrinho()
    #verificar_item_removido()
    time.sleep(2)


@then(u'o usuário voltará para pagina de inventário')
def voltar_pagina_inventário(context):
    pagina_inventario()
    time.sleep(2)