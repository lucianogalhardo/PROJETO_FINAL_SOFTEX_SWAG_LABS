import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.base_page import *
from features.pages.ploblem_user_page import clicar_botao_login, preencher_dados_usuario, logout_usuario

@given(u'que o usuário está na página de login')
def acessar_site_aplicacao(context):
    get_driver().get("https://www.saucedemo.com/")

@when(u'o usuário inserir o user_nme "problem_user" e password "secret_sauce"')
def preencher_campos_login(context):
    preencher_dados_usuario()
    
@when(u'clica no botão de login')
def clicar_botao_acessar(context):
    clicar_botao_login()
    
    # Apresenta posição do mouse para referência
    #print_mouse_position()
    # Chama a função para clicar na opção A
    click_poupup("opcao_a") 
    # Espera para evitar problemas de sincronização

@then(u'o usuário deve ser redirecionado para a página de inventário')
def verificar_login(context):
    assert "Product" in get_element_text("#header_container > div.header_secondary_container > span.title")

@then(u'em seguida o sistema realiza o logout do usuário.')
def realizar_logout(context):
    logout_usuario()
    url_atual = get_driver().current_url
    assert "www.saucedemo.com/" in url_atual, "O título da página não corresponde ao esperado."
