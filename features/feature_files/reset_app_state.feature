Funcionalidade: Menu lateral do sistema Opcao "About"
  

  Contexto:
    Dado que o usuário está na página de login
    Quando o usuário inserir o user_nme "problem_user" e password "secret_sauce"
    E clica no botão de login

  @smoke  @reset
  Cenário: Resetar o estado do sistema através da opção "Reset app state" no menu lateral
    Quando depois que o usuário adiconar item ao carrinho e clica no menu e seleciona a opção "Reset app state"
    Então o sistema deve limpar o carrinho e mudar o botão para "Add to cart"  
  