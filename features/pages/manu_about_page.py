
from features.helpers.driver import get_driver
from features.pages.base_page import *
from selenium.webdriver.support.ui import Select
import time


# Mapeamento de campos para interação
MENU_LATERAL = "#react-burger-menu-btn"
OPCAO_ABOUT = "#about_sidebar_link"

# Variáveis globais
site_oficial_saucelabs = "https://saucelabs.com/" 

# Encapsulamento das ações de interação com a página
def clicar_opcao_about():
    find_element(MENU_LATERAL).click()
    time.sleep(2)  # Espera para evitar problemas de sincronização
    find_element(OPCAO_ABOUT).click()
    time.sleep(2)  # Espera para evitar problemas de sincronização

def verificar_redirecionamento_saucelabs():
    url_atual = get_driver().current_url
    assert site_oficial_saucelabs == url_atual, "O usuário não foi redirecionado para a página oficial do SauceLabs."
    time.sleep(2)  # Espera para evitar problemas de sincronização

