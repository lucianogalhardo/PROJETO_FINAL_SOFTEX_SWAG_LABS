from behave import given, when, then
from features.pages.visual_user_login_page import *


@given('que o usuário está na página de login')
def step_acessar_login(context):
    acessar_page()

@when('o usuário inserir o Username "visual_user" e Password "secret_sauce"')
def step_inserir_dados(context):
    inserir_credenciais("visual_user", "secret_sauce")

@when('clica no botão de login')
def step_clicar_login(context):
    clicar_botao_login()

@then('o usuário deve ser redirecionado para a página de inventário')
def step_validar_login(context):
    validar_pagina_inventario()


