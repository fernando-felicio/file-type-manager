import os
import tempfile
import shutil
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Obter a pasta enviada pelo usuário
        pasta_enviada = request.files["file"]
        if pasta_enviada:
            # Obter o diretório do desktop do usuário
            desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")

            # Criar um diretório temporário único e seguro no desktop do usuário
            caminho_temporario = tempfile.mkdtemp(dir=desktop)

            # Salvar a pasta enviada no diretório temporário
            pasta_enviada.save(os.path.join(caminho_temporario, pasta_enviada.filename))

            # Processar a pasta enviada
            caminho = caminho_temporario
            lista_arquivo = os.listdir(caminho)

            locais = {
                "Imagens": [".jpg", ".jpeg", ".png", ".raw"],
                "Planilhas": [".xls", ".xlsx", ".csv"],
                "Audios": [".mp3"],
                "Videos": [".mp4", ".vid"],
                "PDF's": [".pdf"],
                "Textos": [".docx"],
                "Executaveis": [".exe"],
                "Compactados": [".rar", ".zip"],
                "Arquivos SVG": [".svg"]
            }

            for arquivo in lista_arquivo:
                nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
                for pasta in locais:
                    if extensao in locais[pasta]:
                        if not os.path.exists(f"{caminho}/{pasta}"):
                            os.mkdir(f"{caminho}/{pasta}")
                        os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
