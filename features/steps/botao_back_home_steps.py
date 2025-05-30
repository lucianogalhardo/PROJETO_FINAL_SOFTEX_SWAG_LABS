from behave import given, when, then
from features.pages.visual_user_login_page import realizar_login
from features.pages.botao_back_home_page import *



@given('o usuário acessa o carrinho com 1 item adicionado')
def step_adiciona_item(context):
    acessar_carrinho_com_um_item()


@given('na página de Resumo do Pedido clica no botão "Finish"')
def step_finalizar(context):
    clicar_finish()


@given('o sistema exibe a página de confirmação do pedido com a mensagem "Thank you for your order!"')
def step_valida_mensagem(context):
    validar_mensagem_confirmacao()


@when('o usuário clica no botão "Back Home"')
def step_clica_back_home(context):
    clicar_botao_back_home()


@then('o sistema deve redirecionar o usuário para a página de inventário')
def step_valida_redirecionamento(context):
    validar_redirecionamento_para_inventario()
