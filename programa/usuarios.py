ARQUIVO = "usuarios.txt"

def cadastrar_usuario():
    
    usuario = input("Digite seu usuário: ")
    senha = input("Crie a sua senha: ")

    arquivo = open(ARQUIVO, "r")

    for linha in arquivo:

        dados = linha.split(";") 

        usuario_existente = dados[0] # Linha 12-14: Apoio de IA, pois não sabia como diferenciar um usuário já existente.
        
        if usuario == usuario_existente:
            print("Esse usuário já existe.")
            arquivo.close()
            return
        
    arquivo.close()

    arquivo = open(ARQUIVO, "a")

    arquivo.write(usuario + ";" + senha + "\n")

    arquivo.close()

    print("Usuário cadastrado!")


def login():

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    arquivo = open(ARQUIVO, "r")

    for linha in arquivo:
        
        dados = linha.split(";")

        usuario_arquivo = dados[0]
        senha_arquivo = dados[1]

        if senha_arquivo == senha + "\n":
            
            if usuario == usuario_arquivo:
                print("Login realizado!")
                arquivo.close()
                return
            
    arquivo.close()

    print("Usuário ou senha incorretos.")
    