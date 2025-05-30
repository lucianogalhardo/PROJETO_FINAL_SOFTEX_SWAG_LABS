from behave import given, when, then
from features.pages.mudar_btn_ao_clicar_page import *


@when(u'o usuário clica em "Add to cart" no produto "Sauce Labs Onesie"')
def adicionar_body(context):
    adicionar_sauce_labs_onesie()


@then(u'o botão deve mudar para "{mensagem_correta}"')
def validar_mudanca_btn(context, mensagem_correta):
    assert verificar_botao_mudou() == mensagem_correta