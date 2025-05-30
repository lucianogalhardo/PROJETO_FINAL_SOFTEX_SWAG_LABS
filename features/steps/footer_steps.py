from behave import given, when, then
from features.pages import login_page, footer_page
from features.helpers.driver import get_driver
from features.pages.base_page import click_poupup
from selenium.webdriver.common.by import By
import pyautogui
import time

@given(u'que o usuário está logado como "standard_user"')
def acessar_usuario(context):
    login_page.login_usuario("standard_user")
    time.sleep(5)
    
    click_poupup("opcao_a")


@when('ele visualiza a página de inventário')
def visualizar_inventario(context):
    assert "inventory" in context.driver.current_url
    time.sleep(3)


@when('clicar nos ícones de "Twitter" "Facebook" e "Linkedin"')
def clicar_icones_redes_sociais(context):
    context.links = footer_page.clicar_icones_footer()
    time.sleep(3)


@then('deve ser direcionado corretamente para a página correspondente de cada rede social')
def validar_redes(context):
    print("Links capturados:", context.links) 
    assert "twitter.com" in context.links["Twitter"]
    assert "facebook.com" in context.links["Facebook"]
    assert "linkedin.com" in context.links["Linkedin"]
