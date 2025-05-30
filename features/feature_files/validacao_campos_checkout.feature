Funcionalidade: Validação de campos obrigatórios no checkout

Como usuário do Swag Labs
Quero ser informado quando campos obrigatórios não forem preenchidos no checkout
Para que eu possa completar corretamente minhas informações antes de finalizar a compra

Contexto: Logar na aplicação
  Dado que o usuário acessa a página de login
  Quando o usuário preenche o usuário "error_user" e a senha "secret_sauce"
  Então o usuário deve ser redirecionado para a tela de inventário

 @validacao @funcional
  Cenário: Usuário tenta avançar sem preencher o sobrenome
    Dado o usuário adiciona o produto "Sauce Labs Bolt T-Shirt" ao carrinho para validação
    E o usuário acessa o carrinho e clica em "Checkout"
    Quando o usuário preenche apenas o primeiro nome e o CEP
    E clica em "Continue"
    Então deve ser exibida a mensagem de erro "Error: Last Name is required"