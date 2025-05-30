
from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select
import time
    
# Mapeamento de campos para interação
CAMPO_NOME = "#user-name"
CAMPO_PASSWORD = "#password"
BOTAO_LOGIN = "#login-button"
MENU_LATERAL = "#react-burger-menu-btn"
OPCAO_LOGOUT = "#logout_sidebar_link"

# Variáveis globais
user_name = "problem_user"
password = "secret_sauce"

# Encapsulamento das ações de interação com a página
def preencher_dados_usuario():
    preencher_campo_usuario()
    preencher_campo_senha()

def logout_usuario():
    menu_lateral()
    opcao_logout()
        

def preencher_campo_usuario():
    find_element(CAMPO_NOME).send_keys(user_name)

def preencher_campo_senha():
    find_element(CAMPO_PASSWORD).send_keys(password)
    time.sleep(2)  # Espera para evitar problemas de sincronização
    
def clicar_botao_login():
    find_element(BOTAO_LOGIN).click()
    time.sleep(2)  # Espera para evitar problemas de sincronização

def menu_lateral():
    find_element(MENU_LATERAL).click()
    time.sleep(2)  # Espera para evitar problemas de sincronização

def opcao_logout():
    find_element(OPCAO_LOGOUT).click()
    time.sleep(2)  # Espera para evitar problemas de sincronização



