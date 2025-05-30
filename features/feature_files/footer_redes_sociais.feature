Funcionalidade: Validar o direcionamento para redes sociais através do Footer

    @Footer_test
    Cenário:
        Dado que o usuário está logado como "standard_user"
        Quando ele visualiza a página de inventário
        Quando clicar nos ícones de "Twitter" "Facebook" e "Linkedin"
        Então deve ser direcionado corretamente para a página correspondente de cada rede social