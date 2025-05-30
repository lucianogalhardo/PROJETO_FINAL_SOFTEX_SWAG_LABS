Funcionalidade: Validação do botão "Continue Shopping" na tela do carrinho
  Como um usuário
  Quero clicar no botão "Continue Shopping"
  Para voltar à página de inventário

@botao_continue_shopping
Cenário: Validar botão Continue Shopping
  Dado que o usuário está logado com "visual_user"
  E o usuário acessa o carrinho
  Quando o usuário clica no botão "Continue Shopping"
  Então o usuário deverá ser redirecionado para a página de inventário