Funcionalidade: Cancelar um checkout e voltar ao carrinho

Como usuário do Swag Labs
Quero que o botão "Add to cart" mude para "Remove" após adicionar um produto ao carrinho
Para que eu possa saber que o produto já foi adicionado

Contexto: Logar na aplicação
  Dado que o usuário acessa a página de login
  Quando o usuário preenche o usuário "error_user" e a senha "secret_sauce"
  Então o usuário deve ser redirecionado para a tela de inventário

@testando
Cenário: Usuário cancela o processo de checkout
  Given o usuário adicionou um produto ao carrinho e iniciou o checkout
  When o usuário clica no botão "Cancel"
  Then o usuário deve ser redirecionado de volta para a tela de carrinho