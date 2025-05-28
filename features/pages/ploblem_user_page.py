
from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select
import pyautogui
import time


def click_poupup(opcao):
    if (opcao == "opcao_a"):
        pyautogui.click(935, 411)
    elif (opcao == "opcao_b"):
        pyautogui.click(935, 411)
    
# Mapeamento de campos para interação
CAMPO_NOME = "#user-name"
CAMPO_PASSWORD = "#password"
BOTAO_LOGIN = "#login-button"

# Variáveis globais
user_name = "problem_user"
password = "secret_sauce"

# Encapsulamento das ações de interação com a página
def preencher_dados_usuario():
    preencher_campo_usuario()
    preencher_campo_senha()
        

def preencher_campo_usuario():
    find_element(CAMPO_NOME).send_keys(user_name)

def preencher_campo_senha():
    find_element(CAMPO_PASSWORD).send_keys(password)
    time.sleep(5)  # Espera para evitar problemas de sincronização
    
def clicar_botao_login():
    find_element(BOTAO_LOGIN).click()
    time.sleep(5)  # Espera para evitar problemas de sincronização

# Chama a função para clicar na opção A
click_poupup("opcao_a") 

