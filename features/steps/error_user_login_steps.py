from behave import given, when, then
from features.pages.error_user_login_page import *
from features.pages.base_page import * #clicar_alert_chrome
import time

@given(u'que o usuário acessa a página de login')
def step_acessar_pagina_login(context):
    acessar_pagina_login()

@when(u'o usuário preenche o usuário "{usuario}" e a senha "{senha}"')
def step_login_usuario(context, usuario, senha):
    realizar_login(usuario, senha)
    time.sleep(2)
    #clicar_alert_chrome("janielson")
    click_poupup("janielson")

@then(u'o usuário deve ser redirecionado para a tela de inventário')
def step_redirecionado_inventario(context):
    assert "inventory" in get_driver().current_url
    print("-----------")