ARQUIVOS_PLAYLISTS = "favoritos.txt"

def adc_video_playlist(usuario, id_video):
    playlist = input("Nome da playlist: ")
    arquivo = open(ARQUIVOS_PLAYLISTS, "a")
    arquivo.write(usuario + ";" + playlist + ";" + id_video + "\n")
    arquivo.close()
    print("Vídeo adicionado à playlist.")

def listar_playlists(usuario):
    arquivo = open(ARQUIVOS_PLAYLISTS, "r")
    print("\n--- SUAS PLAYLISTS ---\n")
    
    for linha in arquivo:
        dados = linha.split(";")
        if len(dados) < 3:
            continue
        usuario_arquivo = dados[0]

        if usuario == usuario_arquivo:
            print("Playlist:", dados[1])
            print("ID Vídeo:", dados[2])

            print("---------------------------")
    
    arquivo.close()

def remover_video_playlist(usuario):
    playlist = input("Nome da playlist: ")
    id_video = input("ID do vídeo: ")

    arquivo = open(ARQUIVOS_PLAYLISTS, "r")
    linhas = arquivo.readlines()
    arquivo.close()
    arquivo = open(ARQUIVOS_PLAYLISTS, "w")
    removido = False
    for linha in linhas:
        dados = linha.split(";")
        if len(dados) < 3:
            continue
        usuario_arquivo = dados[0]
        playlist_arquivo = dados[1]

        if usuario == usuario_arquivo and playlist == playlist_arquivo:
            removido = True
        else:
            arquivo.write(linha)
    arquivo.close()

    if removido:
        print("Playlist excluída.")
    else:
        print("Playlist não encontrada.")

def excluir_playlist(usuario):
    playlist = input("Nome da playlist: ")
    arquivo = open(ARQUIVOS_PLAYLISTS, "r")
    linhas = arquivo.readlines()
    arquivo.close()
    arquivo = open(ARQUIVOS_PLAYLISTS, "w")
    removido = False
    for linha in linhas:
        dados = linha.split(";")
        if len(dados) < 3:
            continue
        usuario_arquivo = dados[0]
        playlist_arquivo = dados[1]

        if usuario == usuario_arquivo and playlist == playlist_arquivo:
            removido = True
        else:
            arquivo.write(linha)
    arquivo.close()

    if removido:
        print("Playlist excluída")
    else:
        print("Playlist não encontrada")

def menu_playlists(usuario):
    while True:
        print("\n--- PLAYLISTS ---")
        print("1 - Ver playlists")
        print("2 - Remover vídeos da playlist")
        print("3 - Excluir playlist")
        print("0 - Voltar")

        esc = input("Digite sua escolha: ")

        if esc == "1":
            listar_playlists(usuario)

        elif esc == "2":
            remover_video_playlist(usuario)

        elif esc == "3":
            excluir_playlist(usuario)

        elif esc == "0":
            break