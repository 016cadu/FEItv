from usuarios import cadastrar_usuario, login
from videos import listar_videos, buscar_video

def menu_usuario():
    while True:
        print("\n--- FEItv ---")
        print("1 - Ver catálogo")
        print("2 - Buscar vídeo")
        print("0 - Logout")

        esc = input("Digite sua escolha: ")

        if esc == "1":
            listar_videos()

        elif esc == "2":
            buscar_video()

        elif esc == "0":
            print("Logout realizado!")
            break


while True:
    print("\n--- PÁGINA DE CADASTRO ---")
    print("1 - Cadastrar")
    print("2 - Login")
    print("0 - Sair")

    esc = input("Digite sua escolha: ")

    if esc == "1":
        cadastrar_usuario()

    elif esc == "2":
        acesso = login()
        if acesso == True:
            menu_usuario()

    elif esc == "0":
        print("Sistema encerrado.")
        break
