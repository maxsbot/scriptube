import pandas as pd
from pytube import YouTube


def clean_filename(filename):
    invalid_chars = ["<", ">", ":", '"', "/", "\\", "|", "?", "*"]
    for char in invalid_chars:
        filename = filename.replace(char, "")
    return filename


# Solicita o caminho completo da planilha e o local de armazenamento dos vídeos
planilha_path = input("Por favor, informe o caminho completo da planilha: ")
output_path = input(
    "Por favor, informe o caminho onde os vídeos devem ser armazenados: "
)

# Lê a planilha usando o pandas
df = pd.read_excel(planilha_path)

# Itera sobre as linhas da planilha
for index, row in df.iterrows():
    video_name = clean_filename(row[0])  # limpa o nome do vídeo
    video_url = row[1]  # URL do vídeo está na segunda coluna

    # Acrescenta '.mp4' no final do nome do arquivo
    video_name = f"{video_name}.mp4"

    # Usa a biblioteca pytube para baixar o vídeo
    try:
        yt = YouTube(video_url)
        yt.streams.filter(progressive=True, file_extension="mp4").order_by(
            "resolution"
        ).asc().first().download(output_path=output_path, filename=video_name)
        print(f"Vídeo '{video_name}' baixado com sucesso.")
    except Exception as e:
        print(f"Não foi possível baixar o vídeo '{video_name}'. Erro: {e}")
