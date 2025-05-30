from behave import given, when, then
from features.pages.manu_about_page import clicar_opcao_about, verificar_redirecionamento_saucelabs


@when(u'o usuário clica no menu e seleciona a opção "About"')
def clique_about(context):
    clicar_opcao_about()

@then(u'o sistema deve redirecionar para a página oficial da Sauce Labs')
def verificar_url_saucelabs(context):
    verificar_redirecionamento_saucelabs()