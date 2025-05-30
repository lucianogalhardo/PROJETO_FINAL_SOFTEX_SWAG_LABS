from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages import login_page
from features.helpers import driver
import time

@given(u'que a página de login for acessada')
def acessar_pagina(context):
    login_page.abrir_pagina_login()
    time.sleep(3)

@when(u'o campo de usuário for preenchido com "locked_out_user"')
def preencher_usuario(context):
    login_page.preencher_usuario("locked_out_user")
    time.sleep(3)

@when(u'o campo de senha com "secret_sauce"')
def preencher_senha(context):
    login_page.preencher_senha("secret_sauce")
    login_page.clicar_botao_login()
    time.sleep(3)

@then(u'uma mensagem de erro deve ser exibida')
def mensagem_erro(context):
    erro = login_page.buscar_mensagem_erro()
    assert "Epic sadface: Sorry, this user has been locked out." in erro
    time.sleep(3)

@then('o usuário deve permanecer na mesma página')
def permanecer_na_pagina(context):
    assert login_page.esta_na_pagina_login(), "o usuário foi redirecionado incorretamente"




