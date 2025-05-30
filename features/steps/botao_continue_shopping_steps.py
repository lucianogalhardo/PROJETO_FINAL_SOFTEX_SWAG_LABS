from behave import given, when, then
from features.pages.visual_user_login_page import realizar_login
from features.pages.botao_continue_shopping_page import *


@given('o usuário acessa o carrinho')
def step_acessar_carrinho(context):
    acessar_carrinho()


@when('o usuário clica no botão "Continue Shopping"')
def step_clica_continue_shopping(context):
    clicar_continue_shopping()
