'''
Extração de links de download de vídeos do vimeo

- Precisamos pegar os links em 1080p, 720p e 540p para importar os vídeos para uma nova plataforma
'''

# Dicionário Vimeo
from dic_vimeo import dicionario_vimeo

import pprint
videos = []
informacoes = dicionario_vimeo["data"]

for item in informacoes:
    video_uri = item["uri"]
    nome = item["name"]
    duracao = item["duration"]

    link_540p = ""
    link_720p = ""
    link_1080p = ""

    lista_downloads = item["download"]
    for dicionario_download in lista_downloads:
        if dicionario_download["rendition"] == "540p":
            link_540p = dicionario_download["link"]
        if dicionario_download["rendition"] == "720p":
            link_720p = dicionario_download["link"]
        if dicionario_download["rendition"] == "1080p":
            link_1080p = dicionario_download["link"]

    dicionario_item = {'uri': video_uri, 'nome': nome, 'duracao': duracao, 'link540p': link_540p, 'link720p': link_720p, 'link1080p': link_1080p}
    videos.append(dicionario_item)

pprint.pprint(videos)