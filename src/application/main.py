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
    "Executaveis" : [".exe"]
}