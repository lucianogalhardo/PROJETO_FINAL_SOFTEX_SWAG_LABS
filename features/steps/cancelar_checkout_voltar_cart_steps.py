from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.cancelar_checkout_voltar_cart_page import *
import time

@given("o usuário adicionou um produto ao carrinho e iniciou o checkout")
def fazer_checkout(context):
    ir_para_checkout()

@when('o usuário clica no botão "Cancel"')
def clicar_cancelar(context):
    clicar_btn_cancelar()
    

@then("o usuário deve ser redirecionado de volta para a tela de carrinho")
def voltar_para_carrinho(context):
    esta_na_pagina_de_carrinho()