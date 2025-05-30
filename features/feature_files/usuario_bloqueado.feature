Funcionalidade: Validar que um usuário bloqueado não consegue acessar o sistema

    @Bloqueado_test
    Cenário: Tentativa de login com usuário bloqueado
        Dado que a página de login for acessada
        Quando o campo de usuário for preenchido com "locked_out_user"
        E o campo de senha com "secret_sauce"
        Então uma mensagem de erro deve ser exibida
        E o usuário deve permanecer na mesma página