import os

from tkinter.filedialog import askdirectory

caminho = askdirectory(title= "Selecione uma pasta: ")
print(caminho)

lista_arquivo = os.listdir(caminho)
print(lista_arquivo)

locais = {
    "Imagens" : [".jpg", ".jpeg", ".png", ".raw"],
    "Planilhas" : [".xlss", ".csv"],
    "Audios" : [".mp3"],
    "Videos" :[".mp4", ".vid"],
    "PDF's" : [".pdf"],
    "Textos" : [".docx"],
    "Executaveis" : [".exe"],
    "Compactados":[".rar", ".zip"]
}

for arquivo in lista_arquivo:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/ {arquivo}", f"{caminho}/{pasta}/{arquivo}")
           
