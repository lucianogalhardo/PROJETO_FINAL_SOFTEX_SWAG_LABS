Funcionalidade: Login de usuário
    Como um simples usuário com login "visual_user" e senha "secret_sauce"
    Quero acessar a página de inventário
    Para realizar compras

@visual_login
Cenário: Usuário faz login com sucesso
  Dado que o usuário está na página para login
  Quando o usuário inserir o Username "visual_user" e Password "secret_sauce"
  E clicar no botão de login
  Então o usuário deve ser direcionado para a página de inventário