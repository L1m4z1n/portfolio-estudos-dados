'''
For nos dicionários

Estrutura:

for chave in dicionario:
    faça alguma coisa

'''

vendas_tecnologia = {
                     'iphone': 15000,
                     'samsung galaxy':12000,
                     'tv samsung':10000,
                     'ps5':14300,
                     'notebook':17000,
                     'notebook hp':1000
                     }

# demonstrando o for

for chave in vendas_tecnologia:
    print(f'{chave}: {vendas_tecnologia[chave]}')

#Qual o total de notebooks vendidos
total_notebooks = 0

for chave in vendas_tecnologia:
    if 'notebook' in chave:
        total_notebooks += vendas_tecnologia[chave]
        print(total_notebooks)
