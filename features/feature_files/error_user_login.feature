Funcionalidade: Login no sistema

Como usuário do Swag Labs
Quero fazer login no sistema
Para poder acessar as funcionalidades da aplicação

@smoke @error_login
Cenário: Login com sucesso
  Dado que o usuário acessa a página de login
  Quando o usuário preenche o usuário "error_user" e a senha "secret_sauce"
  Então o usuário deve ser redirecionado para a tela de inventário