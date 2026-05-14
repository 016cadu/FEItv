from usuarios import cadastrar_usuario, login
from videos import listar_videos, buscar_video
from favoritos import menu_playlists

def menu_usuario(usuario):
    while True:
        print("\n--- FEItv ---")
        print("1 - Ver catálogo")
        print("2 - Buscar vídeo")
        print("3 - Gerenciar playlists")
        print("0 - Logout")

        esc = input("Digite sua escolha: ")

        if esc == "1":
            listar_videos(usuario)

        elif esc == "2":
            buscar_video(usuario)

        elif esc == "3":
            menu_playlists(usuario)

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
        usuario_logado = login()
        if usuario_logado:
            menu_usuario(usuario_logado)

    elif esc == "0":
        print("Sistema encerrado.")
        break
