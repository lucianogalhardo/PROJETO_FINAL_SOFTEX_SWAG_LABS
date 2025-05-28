Funcionalidade: Login de usuário
    Como um simples usuário com login "problem_user" e senha "secret_sauce"
    Quero acessar a página de inventário
    Para reliazer compras

@smoke
Cenário: Usuário faz login com sucesso
  Dado que o usuário está na página de login
  Quando o usuário inserir o user_nme "problem_user" e password "secret_sauce"
  E clica no botão de login
  Então o usuário deve ser redirecionado para a página de inventário