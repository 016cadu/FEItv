from curtidas import curtir_video, descurtir_video
from favoritos import adc_video_playlist

ARQUIVO_VIDEOS = "videos.txt"

def menu_video(usuario, id_video):
    while True:
        print("\n1 - Curtir")
        print("2 - Descurtir")
        print("3 - Adicionar à playlist")
        print("0 - Voltar")

        esc = input("Escolha: ")

        if esc == "1":
            curtir_video(usuario, id_video)

        elif esc == "2":
            descurtir_video(usuario, id_video)

        elif esc == "3":
            adc_video_playlist(usuario, id_video)

        elif esc == "0":
            break

def listar_videos(usuario):
    arquivo = open(ARQUIVO_VIDEOS, "r")

    print("\n--- CATÁLOGO FEITV ---\n")

    for linha in arquivo:
        
        dados = linha.split(";")
        if len(dados) < 6:
            continue
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

    id_video = input("\nDigite o ID do vídeo (0 para voltar): ")

    if id_video != "0":
        menu_video(usuario, id_video)

def buscar_video(usuario):
    busca = input("Digite o nome do filme: ")
    arquivo = open(ARQUIVO_VIDEOS, "r")

    encontrado = False

    for linha in arquivo:
        dados = linha.split(";")
        if len(dados) < 6:
            continue
        id_video = dados[0]
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

            menu_video(usuario, id_video)

    arquivo.close()

    if encontrado == False:
        print("Filme não encontrado :(")