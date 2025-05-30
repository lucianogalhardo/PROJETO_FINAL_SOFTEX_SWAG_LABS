from behave import given, when, then
from features.pages import login_page
from features.pages import mensagem_page  
from features.pages import base_page
from features.pages.base_page import click_poupup
from selenium.webdriver.common.by import By
import pyautogui
import time

@given(u'que o usuário esteja logado com o usuário "standard_user"')
def acessar_usuario(context):
    login_page.login_usuario("standard_user")
    time.sleep(3)

    click_poupup("ana")
    time.sleep(3)


@given(u'tiver adicionado um produto ao carrinho')
def adicionar_produto(context):
    mensagem_page.adicionar_item_ao_carrinho()
    mensagem_page.ir_para_checkout()
    time.sleep(3)


@when(u'preencher os campos de checkout e clicar em "Continue"')
def preencher_checkout(context):
    mensagem_page.preencher_checkout("Ana", "Rita", "12345")
    time.sleep(3)


@when(u'na próxima página clicar no botão "Finish"')
def clicar_botao_finish(context):
    mensagem_page.finalizar_compra()
    time.sleep(3)


@then(u'uma mensagem de sucesso deve ser exibida')
def verificar_mensagem(context):
    mensagem = context.driver.find_element(By.CLASS_NAME, "complete-header").text
    print(f"Mensagem capturada: {mensagem}")
    assert mensagem is not None, "a mensagem de sucesso não foi encontrada na página"
    assert "Thank you for your order!" in mensagem


