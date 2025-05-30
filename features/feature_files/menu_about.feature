Funcionalidade: Menu lateral do sistema Opcao "About"

  Contexto:
    Dado que o usuário está na página de login
    Quando o usuário inserir o user_nme "problem_user" e password "secret_sauce"
    E clica no botão de login

  @smoke  @about
  Cenário: Acessar a página "About" pelo menu lateral
    Quando o usuário clica no menu e seleciona a opção "About"
    Então o sistema deve redirecionar para a página oficial da Sauce Labs