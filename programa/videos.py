ARQUIVO_VIDEOS = "videos.txt"

def listar_videos():
    arquivo = open(ARQUIVO_VIDEOS, "r")

    print("\n--- CATÁLOGO FEITV ---\n")

    for linha in arquivo:
        
        dados = linha.split(";")
        id_video = dados[0]
        titulo = dados[1]
        duracao = dados[2]
        genero = dados[3]
        diretor = dados[4]
        ano = dados[5]

        print("ID:", id_video)
        print("Título:", titulo)
        print("Duração;", duracao, "minutos")
        print("Gênero:", genero)
        print("Diretor:", diretor)
        print("Ano de lançamento:", ano)
        print("---------------------------")

    arquivo.close()

def buscar_video():
    busca = input("Digite o nome do filme: ")
    arquivo = open(ARQUIVO_VIDEOS, "r")

    encontrado = False

    for linha in arquivo:
        dados = linha.split(";")
        titulo = dados[1]

        if busca.lower() in titulo.lower():
            encontrado = True
            print("\nVídeo encontrado\n")

            print("ID:", dados[0])
            print("Título:", dados[1])
            print("Duração:", dados[2], "min")
            print("Gênero:", dados[3])
            print("Diretor:", dados[4])
            print("Ano:", dados[5])
            print("---------------------------")

    arquivo.close()

    if encontrado == False:
        print("Filme não encontrado :(")