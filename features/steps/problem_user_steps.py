import time
from behave import given, when, then
from features.helpers.driver import get_driver
from features.pages.base_page import *
from features.pages.ploblem_user_page import preencher_dados_usuario


@given(u'que o usuário está na página de login')
def acessar_site_aplicacao(context):
    get_driver().get("https://www.saucedemo.com/")

@when(u'o usuário inserir o user_nme "problem_user" e password "secret_sauce"')
def preencher_campos_login(context):
    preencher_dados_usuario()
    
@when(u'clica no botão de login')
def step_impl(context):
    raise NotImplementedError(u'STEP: When clica no botão de login')


@then(u'o usuário deve ser redirecionado para a página de inventário')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then o usuário deve ser redirecionado para a página de inventário')

