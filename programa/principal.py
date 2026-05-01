from usuarios import cadastrar_usuario, login

while True:
    print("\n--- FEItv ---")
    print("1 - Cadastrar")
    print("2 - Login")
    print("0 - Sair")

    esc = input("Digite sua escolha: ")

    if esc == "1":
        cadastrar_usuario()

    elif esc == "2":
        login()

    elif esc == "0":
        break