from behave import given, when, then
from features.pages.visual_user_login_page import *
from features.pages.base_page import *


@given('que o usuário está na página para login')
def step_acessar_login(context):
    acessar_page()

@when('o usuário inserir o Username "{usuario}" e Password "{senha}"')
def step_inserir_dados(context, usuario, senha):
    inserir_credenciais(usuario, senha)

@when('clicar no botão de login')
def step_clicar_login(context):
    clicar_botao_login()
    click_poupup("opcao_a")


@then('o usuário deve ser direcionado para a página de inventário')
def step_validar_login(context):
    validar_pagina_inventario()


