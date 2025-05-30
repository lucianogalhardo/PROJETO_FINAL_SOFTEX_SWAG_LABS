Funcionalidade: Finalizar compra sem itens no carrinho
  Como um usuário logado
  Quero finalizar uma compra sem itens
  Para verificar se o sistema permite esse comportamento inesperado

@finalizar_compra_sem_itens
Cenário: Finalizar compra com sucesso sem itens no carrinho
  Dado que o usuário está logado com "visual_user"
  E o usuário acessa o carrinho sem adicionar produtos
  E clica no botão "Checkout"
  E na página de informações do usuário preenche os campos: Primeiro Nome: "Leonardo", Sobrenome: "da Silva", CEP: "12345"
  E clica no botão "Continue"
  Quando clica no botão "Finish" na página de Resumo do Pedido
  Então o sistema deve exibir a página de confirmação do pedido com a mensagem "Thank you for your order!"
