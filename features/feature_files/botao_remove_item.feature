Funcionalidade: Remoção de produto do carrinho através do botão "Remove"

  Contexto:
    Dado que o usuário está na página de login
    Quando o usuário inserir o user_nme "problem_user" e password "secret_sauce"
    E clica no botão de login

  @smoke  @remover_item
  Cenário: Remover o produto "Sauce Labs BackPack" do carrinho
    Dado que o usuário adicionou o produto "Sauce Labs BackPack" clicando no botão "Add to cart"
    Quando o usuário acessar a página do carrinho clicar no botão "Remove" do produto "Sauce Labs BackPack"
    Então o produto escolhido será removido do carrinho
    E o usuário voltará para pagina de inventário

