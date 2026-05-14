ARQUIVO_CURTIDAS = "curtidas.txt"

def curtir_video(usuario, id_video):
    arquivo = open(ARQUIVO_CURTIDAS, "r")

    for linha in arquivo:
        dados = linha.split(";")
        if len(dados) < 2:
            continue
        usuario_arquivo = dados[0]
        video_arquivo = dados[1]

        if usuario == usuario_arquivo and id_video + "\n" == video_arquivo:
            print("Você já curtiu esse vídeo.")

            arquivo.close()
            return
        
    arquivo.close()
    arquivo = open(ARQUIVO_CURTIDAS, "a")
    arquivo.write(usuario + ";" + id_video + "\n")
    arquivo.close()
    print("Vídeo curtido.")

def descurtir_video(usuario, id_video):
    arquivo = open(ARQUIVO_CURTIDAS, "r")
    linhas = arquivo.readlines()
    arquivo.close()
    arquivo = open(ARQUIVO_CURTIDAS, "w")
    removido = False
    
    for linha in linhas: 
        dados = linha.split(";")
        if len(dados) < 2:
            continue

        usuario_arquivo = dados[0]
        video_arquivo = dados[1]

        if usuario == usuario_arquivo and id_video + "\n" == video_arquivo:
            removido = True
        else:
            arquivo.write(linha)

    arquivo.close()

    if removido: 
        print("Curtida removida.")
    else:
        print("Você ainda não curtiu esse vídeo.")