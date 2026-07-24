'''
Métodos úteis em dicionários
items() dos dicionários

Estrutura:

itens_dicionario = dicionario.items()

ou então:

for item in dicionario.items()
    cada item do dicionario em formato de tupla
'''

vendas_tecnologia = {
                     'iphone': 15000,
                     'samsung galaxy':12000,
                     'tv samsung':10000,
                     'ps5':4300,
                     'notebook':1300,
                     'notebook hp':1000
                     }

# Quais produtos venderam mais de 5000 unidades

for item,qtde in vendas_tecnologia.items():
    print(f'{item}: {qtde} unidades')

# forma 1 -> usando apenas o dicionario e as chaves
for chave in vendas_tecnologia:
    if vendas_tecnologia[chave] > 5000:
        print(f'{chave}: {vendas_tecnologia[chave]} unidades')


# forma 2 -> usando o dicionario.items()

for produto, qtde in vendas_tecnologia.items():
    if qtde > 5000:
        print(f'{produto}: {qtde} unidades')

'''
Listas importantes a partir do dicionário

Métodos importantes:
.keys() -> uma "lista" com todas as chaves do dicionário

.values() -> uma "lista" com todos os valores do dicionário

Obs:. Se o dicionário for modificado, automaticamente essas variáveis são modificadas, mesmo tendo sido criadas anteriormente
'''

chaves = vendas_tecnologia.keys()
valores = vendas_tecnologia.values()
print(chaves)
print(valores)

vendas_tecnologia['liraphone'] = 10
print(chaves)
print(valores)
print(list(chaves))
print(list(valores))

# organizar lista
lista_chaves = list(chaves)
lista_chaves.sort()

for chave in lista_chaves:
    print(f'{chave}: {vendas_tecnologia[chave]}')