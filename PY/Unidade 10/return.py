# Retornar um número

def minha_soma(num1,num2,num3):
    return num1 + num2 + num3


# Retornar um texto
def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace("  ", " ")
    texto = texto.strip()
    return texto

# Retornar um boolean
def bateu_meta(vendas,meta):
    if vendas >= meta:
        return True
    else:
        return False

# Retornar uma lista, tupla ou dicionário
def filtrar_lista_texto(lista,pedaco_texto):
    lista_filtrada = []
    for item in lista:
        if pedaco_texto in item:
            lista_filtrada.append(item)
    return lista_filtrada

lista_textos = ['lira@gmail.com','zezinho@gmail.com', 'joao@hotmail.com','alon@gmail.com']

lista = filtrar_lista_texto(lista_textos, 'gmail')
print(lista)