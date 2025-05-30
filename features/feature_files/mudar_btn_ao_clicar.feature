Funcionalidade: Mudança de botão após adicionar produto ao carrinho

Como usuário do Swag Labs
Quero que o botão "Add to cart" mude para "Remove" após adicionar um produto ao carrinho
Para que eu possa saber que o produto já foi adicionado

Contexto: Logar na aplicação
  Dado que o usuário acessa a página de login
  Quando o usuário preenche o usuário "error_user" e a senha "secret_sauce"
  Então o usuário deve ser redirecionado para a tela de inventário

 @ui @funcional
  Cenário: Verifica se o botão muda para "Remove" após adicionar produto ao carrinho
    Quando o usuário clica em "Add to cart" no produto "Sauce Labs Onesie"
    Então o botão deve mudar para "Remove"