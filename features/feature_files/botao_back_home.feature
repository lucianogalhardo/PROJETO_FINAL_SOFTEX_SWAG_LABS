Funcionalidade: Validação do botão "Back Home"
  Como um usuário que finalizou uma compra
  Quero poder retornar para a página de inventário
  Para continuar navegando ou comprando mais produtos

Contexto:
  Dado que o usuário está na página para login
  Quando o usuário inserir o Username "visual_user" e Password "secret_sauce"
  E clicar no botão de login
  Então o usuário deve ser direcionado para a página de inventário


@smoke_botao_back_home
Cenário: Validar redirecionamento ao clicar no botão "Back Home"
  Dado que o usuário está logado com "visual_user"
  E o usuário acessa o carrinho com 1 item adicionado
  E clica no botão "Checkout"
  E na página de informações do usuário preenche os campos: Primeiro Nome: "Leonardo", Sobrenome: "da Silva", CEP: "12345"
  E clica no botão "Continue"
  E na página de Resumo do Pedido clica no botão "Finish"
  E o sistema exibe a página de confirmação do pedido com a mensagem "Thank you for your order!"
  Quando o usuário clica no botão "Back Home"
  Então o sistema deve redirecionar o usuário para a página de inventário
