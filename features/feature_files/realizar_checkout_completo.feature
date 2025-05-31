@teste2
Funcionalidade: Realizar checkout completo

Como um usuário do site Swag Labs
Quero finalizar a compra de um produto
Para receber meu pedido com sucesso

Contexto: Logar na aplicação
  Dado que o usuário acessa a página de login
  Quando o usuário preenche o usuário "error_user" e a senha "secret_sauce"
  Então o usuário deve ser redirecionado para a tela de inventário

 @smoke_aceitacao
  Cenário: Usuário finaliza uma compra com sucesso
    Dado o usuário adiciona o produto "Sauce Labs Backpack" ao carrinho
    Quando o usuário acessa o carrinho e clica em "Checkout"
    E o usuário preenche os campos Nome, Sobrenome e CEP
    E o usuário clica em "Continue" e depois em "Finish"
    Então a mensagem "Thank you for your order!" deve ser exibida
