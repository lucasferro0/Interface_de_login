from tkinter import *
from tkinter import messagebox
import os
import mysql.connector


def bd():
    con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="cadastro"
                )
    return con


def tela_login():
    
    def tela_3():

        def validar():
            if nome_entrada.get() == "" or (nome_entrada.get()).isspace() or data_entrada.get() == "" or (data_entrada.get()).isspace() or telefone_entrada.get() == "" or (telefone_entrada.get()).isspace() or email_entrada.get() == "" or (email_entrada.get()).isspace() or bairro_entrada.get() == "" or (bairro_entrada.get()).isspace() or cidade_estado_entrada.get() == "" or (cidade_estado_entrada.get()).isspace():
                status = messagebox.showinfo(title="", message="Algo deu errado, tente novamente.")
                return
            else:
                return "Pode continuar"


        def cadastrar_cliente():
            # CONECTANDO AO BANCO DE DADOS
            try:
                con = bd()
            except:
                status = messagebox.showinfo(title="", message="Ocorreu um erro ao conectar com banco de dados.")
            else:
                if con.is_connected():
                    status = validar()
                    if status == None:
                        con.close()
                    else:
                        cursor = con.cursor()
                        try:
                            data = data_entrada.get()
                            dd, mm, aa = data.split("/")
                            data_formatada = f"{aa}/{mm}/{dd}"
                            cursor.execute(f'insert into clientes (nome, data_de_nascimento, telefone, email, bairro, cidade_estado) values ("{nome_entrada.get()}", "{data_formatada}", "{telefone_entrada.get()}", "{email_entrada.get()}", "{bairro_entrada.get()}", "{cidade_estado_entrada.get()}");')
                        except:
                            messagebox.showinfo(title="", message="Algo deu errado, tente novamente.")
                            cursor.close()
                            con.close()
                        else:
                            status = messagebox.showinfo(title="", message="Dados salvos com sucesso!")
                            con.close()
                            cursor.close()
                else:
                    status = messagebox.showinfo(title="", message="Ocorreu um erro ao conectar com banco de dados.")
        

        # INTERFACE GRÁFICA

        tela = Tk()

        tela.title("Cadastro de clientes")
        tela.geometry("500x400")
        tela.configure(background="#BFDBFA")
        tela.iconbitmap("images/favicon.ico")

        principal = Label(tela,text="Cadastro de clientes",background="#BFDBFA", font="timesnewroman 15 bold", foreground="gray")
        principal.place(x=160,y=8)

        nome = Label(tela,text="Nome do cliente:", background="#BFDBFA",font="timesnewroman 10 bold")
        nome.place(x=10,y=60)

        nome_entrada = Entry(tela, width=50)
        nome_entrada.place(x=130,y=63)

        data_de_nascimento = Label(tela,text="Data de nascimento:", background="#BFDBFA",font="timesnewroman 10 bold")
        data_de_nascimento.place(x=10,y=100)

        data_entrada = Entry(tela, width=20)
        data_entrada.place(x=150,y=103)

        telefone = Label(tela,text="Telefone:", background="#BFDBFA",font="timesnewroman 10 bold")
        telefone.place(x=10,y=140)

        telefone_entrada = Entry(tela,width=25)
        telefone_entrada.place(x=80,y=143)

        email = Label(tela, text="E-mail:", background="#BFDBFA",font="timesnewroman 10 bold")
        email.place(x=10,y=180)

        email_entrada= Entry(tela,width=40)
        email_entrada.place(x=63,y=182)

        bairro = Label(tela, text="Bairro:", background="#BFDBFA",font="timesnewroman 10 bold")
        bairro.place(x=10,y=220)

        bairro_entrada = Entry(tela,width=30)
        bairro_entrada.place(x=63,y=223)

        cidade_estado = Label(tela, text="Cidade-Estado:", background="#BFDBFA",font="timesnewroman 10 bold")
        cidade_estado.place(x=10,y=260)

        cidade_estado_entrada = Entry(tela,width=30)
        cidade_estado_entrada.place(x=113,y=262)


        cadastrar = Button(tela,text="Cadastrar cliente",command=cadastrar_cliente,background="white")
        cadastrar.place(x=200,y=350)

        # INICIA O PROGRAMA
        tela.mainloop()


    def tela2():
        def fazer_login():
            tela.destroy()
            tela_login()


        def validar():
            if not (user.get()).isidentifier() or password.get() == "" or (password.get()).isspace():
                status = messagebox.showinfo(title=" ", message=" Algo deu errado, tente novamente.")
                return
            else:
                return "pode cadastrar"

        def status():
            status = messagebox.askyesno(title=" ", message="Deseja continuar ?")
            if status == True:
                # VALIDAÇÃO DO QUE FOI DIGITADO
                validando = validar()
                if validando == "pode cadastrar":
                    if password.get() != confirm_senha.get():
                        status = messagebox.showinfo(title="", message="Senhas diferentes.")
                    else:
                        try:
                            con = bd()
                        except:
                            status = messagebox.showinfo(title="", message="Ocorreu um erro ao conectar com o banco de dados.")
                        else:
                            if con.is_connected():
                                lista = []
                                cursor  = con.cursor()
                                cursor.execute("select * from contas;")
                                linhas = cursor.fetchall()
                                if cursor.rowcount > 0:
                                    for l in linhas:
                                        lista.append(l[1])
                                    
                                    if user.get() in lista:
                                        status = messagebox.showinfo(title=" ", message="Usuário já existe!")
                                        con.close()
                                        cursor.close()
                                    else:
                                        cursor.execute(f'insert into contas (login, senha) values("{user.get()}","{password.get()}");')
                                        con.close()
                                        cursor.close()
                                        status = messagebox.showinfo(title=" ", message="Cadastrado com sucesso!")
                                else:
                                    cursor.execute(f'insert into contas (login, senha) values("{user.get()}","{password.get()}");')
                                    con.close()
                                    cursor.close()
                                    status = messagebox.showinfo(title="", message="Cadastrado com sucesso!")
                            else:
                                messagebox.showinfo(title="", message="Ocorreu um erro ao conectar com o banco de dados.")

        # INTERFACE GRÁFICA DA TELA 2
        tela = Tk()

        tela.title("Cadastro")
        tela.geometry("300x200")
        tela.configure(background="#BFDBFA")
        tela.iconbitmap("images/favicon.ico")

        nome = Label(tela,text="Usuário:",background="#BFDBFA")
        nome.place(x=40,y=37)

        image_user = PhotoImage(file="images/user_icon.png")
        logo_user = Label(tela, image=image_user, background="#BFDBFA")
        logo_user.place(x=10,y=37)

        user = Entry(tela, width=25)
        user.place(x=100,y=40)

        senha = Label(tela,text="Senha:",background="#BFDBFA")
        senha.place(x=40,y=78)

        image_password = PhotoImage(file="images/password_icon.png")
        logo_password = Label(tela, image=image_password, background="#BFDBFA")
        logo_password.place(x=10,y=78)

        password = Entry(tela, width=25,show="*")
        password.place(x=100,y=80)

        confirm = Label(tela, text="Confirmar:", background="#BFDBFA" )
        confirm.place(x=30,y=118)

        confirm_senha = Entry(tela, width=25, show="*")
        confirm_senha.place(x=100,y=120)

        cadastrar = Button(tela,text="Cadastrar",command=status,background="white")
        cadastrar.place(x=140,y=150)

        fazer_login = Button(tela,text="Fazer login",command=fazer_login,background="white")
        fazer_login.place(x=10,y=160)

        # INICIA A TELA 2
        tela.mainloop()

    # CÓDIGOS DA TELA DE LOGIN (TELA1)

    #FUNÇÃO PARA CHAMAR A TELA DE CRIAR CONTA (TELA2)
    def criar_conta():
        tela.destroy()
        tela2()

    # FUNÇÃO PARA CHAMAR A TELA DE CADASTRO (TELA3)
    def tela_de_cadastro():
        tela.destroy()
        tela_3()

    def validar():
        if not (user.get()).isidentifier() or password.get() == "" or (password.get()).isspace():
            status = messagebox.showinfo(title=" ", message=" Algo deu errado, tente novamente.")
            return
        else:
            return "Pode efetuar login"


    def verificar_dados():
        try:
            con = bd()
        except:
            messagebox.showinfo(title=" ", message="Ocorreu um erro ao conectar com o banco de dados.")
        else:
            status = validar()
            if status == "Pode efetuar login":
                cursor = con.cursor()
                cursor.execute('select * from contas;')
                linhas = cursor.fetchall()
                if cursor.rowcount > 0:
                    users = []
                    for l in linhas:
                        users.append((l[1],l[2]))
                    for e in users:
                        if e[0] == user.get() and e[1] == password.get():
                            messagebox.showinfo(title="", message="Login efetuado com sucesso!")
                            tela_de_cadastro()
                            achar = True
                            con.close()
                            cursor.close()
                            break
                        else:
                            achar = False
                    if achar == False:
                        con.close()
                        cursor.close()
                        messagebox.showinfo(title="", message="Dados incorretos.")
                else:
                    con.close()
                    cursor.close()
                    messagebox.showinfo(title="", message="Usuário não encontrado.")



    # INTERFACES GRÁFICAS
    tela = Tk()

    tela.title("Login")
    tela.geometry("300x200")
    tela.configure(background="#BFDBFA")
    tela.iconbitmap("images/favicon.ico")

    nome = Label(tela,text="Usuário:",background="#BFDBFA")
    nome.place(x=40,y=37)

    image_user = PhotoImage(file="images/user_icon.png")
    logo_user = Label(tela, image=image_user, background="#BFDBFA")
    logo_user.place(x=10,y=37)

    user = Entry(tela, width=25)
    user.place(x=100,y=40)

    senha = Label(tela,text="Senha:",background="#BFDBFA")
    senha.place(x=40,y=78)

    image_password = PhotoImage(file="images/password_icon.png")
    logo_password = Label(tela, image=image_password, background="#BFDBFA")
    logo_password.place(x=10,y=78)

    password = Entry(tela, width=25, show="*")
    password.place(x=100,y=80)

    Entrar = Button(tela,text="Entrar", command=verificar_dados,background="white")
    Entrar.place(x=140,y=120)

    cadastrar = Button(tela,text="Criar conta",command=criar_conta,background="white")
    cadastrar.place(x=10,y=160)

    # INICIA O PROGRAMA
    tela.mainloop()

tela_login()