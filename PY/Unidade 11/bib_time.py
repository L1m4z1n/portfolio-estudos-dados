import time 
import locale # Ajuda para localizar aonde você quer

locale.setlocale(locale.LC_TIME,"pt_BR")
data_local = time.localtime()
data_texto = time.strftime("%d-%m-%y %A", data_local)

print(data_texto)

# Ler arquivos com datas formatadas de maneira diferente:

lista_datas = ["01 de Junho de 2026","01 de Janeiro de 2027","15 de fevereiro de 2027","18 de dezembro de 2027"]

for data in lista_datas:
    data_estruturada = time.strptime(data,"%d de %B de %Y")
    print(data_estruturada)