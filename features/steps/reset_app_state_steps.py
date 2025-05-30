from behave import given, when, then
from features.pages import *
from features.pages.reset_app_state_page import *


@when(u'depois que o usuário adiconar item ao carrinho e clica no menu e seleciona a opção "Reset app state"')
def adicionar_item(context):
    adicionar_item_ao_carrinho()
    clicar_opcao_reset()


@then(u'o sistema deve limpar o carrinho e mudar o botão para "{texto_correto}"')
def verificar_botao(context, texto_correto):
    assert verificar_status_butao_add() == texto_correto