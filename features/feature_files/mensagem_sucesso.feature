Funcionalidade: Validar a mensagem de sucesso ao realizar compra

    @Mensagem_test
    Cenário: 
        Dado que o usuário esteja logado com o usuário "standard_user"
        E tiver adicionado um produto ao carrinho
        Quando preencher os campos de checkout e clicar em "Continue"
        E na próxima página clicar no botão "Finish"
        Então uma mensagem de sucesso deve ser exibida