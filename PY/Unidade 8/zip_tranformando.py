'''
Transformando Listas em dicionários e Function zip

Estrutura:
- Dicionário com valores padrões:
dicionario = dict.fromkeys(lista_chaves, valor_padrao)

- Dicionário a partir de listas de tuplas:
dicionario = dict(lista_tuplas)

Dicionário a partir de 2 listas:
Passo 1: Transformar lista em listas de tuplas com métodos zip
Passo 2: Transformar em dicionário

lista_tuplas = zip(lista1,lista2) dicionario = dict(lista_tuplas)

'''

produtos = [
                     'iphone',
                     'samsung galaxy',
                     'tv samsung',
                     'ps5',
                     'notebook',
                     'notebook hp'
]
vendas = [5000,3500,6000,3200,4200,1500]

lista_tuplas = zip(produtos,vendas)
dicionario_vendas = dict(lista_tuplas)
print(dicionario_vendas)

# Quantos vendemos de iphone

#fazendo por lista
i = produtos.index('iphone')
print(f'Vendemos {vendas[i]} iphones')

# fazendo por dicionário
print(f'Vendemos {dicionario_vendas['iphone']} iphones')
