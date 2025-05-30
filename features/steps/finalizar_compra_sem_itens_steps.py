from behave import given, when, then
from features.pages.visual_user_login_page import realizar_login
from features.pages.finalizar_compra_sem_itens_page import *
from features.pages.base_page import *

@given('que o usuário está logado com "visual_user"')
def step_login_usuario(context):
    realizar_login("visual_user", "secret_sauce")

@given('o usuário acessa o carrinho sem adicionar produtos')
def step_acessar_carrinho(context):
    acessar_carrinho()

@given('clica no botão "Checkout"')
def step_checkout(context):
    clicar_checkout()

@given('na página de informações do usuário preenche os campos: Primeiro Nome: "Leonardo", Sobrenome: "da Silva", CEP: "12345"')
def step_preencher_dados(context):
    preencher_informacoes_usuario("Leonardo", "da Silva", "12345")

@given('clica no botão "Continue"')
def step_continuar(context):
    clicar_continue()

@when('clica no botão "Finish" na página de Resumo do Pedido')
def step_finalizar(context):
    clicar_finish()

@then('o sistema deve exibir a página de confirmação do pedido com a mensagem "Thank you for your order!"')
def step_validar_mensagem(context):
    validar_mensagem_confirmacao()
