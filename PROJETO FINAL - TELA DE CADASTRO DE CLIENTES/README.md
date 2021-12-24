A largura dos elementos na tela pode ser definidar das seguintes formas:

    user = Entry(tela, width=25)
    user.place(x=100,y=40)

    Ou a largura pode ser definida de uma outra forma:

        user = Entry(tela)
        user.place(x=100,y=40, width=25)


A altura pode ser definida somente dessa forma:

    user = Entry(tela)
    user.place(x=100,y=40, height=20)

Se for querer definir a altura e a largura do elemento, usa das seguintes formas:

    user = Entry(tela, width=25)
    user.place(x=100,y=40, hegith=20)

    Ou pode utilizar dessa outra forma:

        user = Entry(tela)
        user.place(x=100,y=40, width=25, height=20)

Diferença entre as funções .quit() e a .destroy() no tkinter:

    A função .quit(), você utiliza quando estiver trabalhando somente com uma tela

    A função .destroy(), você utiliza quando estiver trabalhando com mais de uma tela

