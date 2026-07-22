'''
Dicionários em Python

Estrutura:
dicionario = {chave: valor, chave: valor, chave: valor...}

Vantagens e Desvantagens:
- Não devem ser usadas para pegar itens em uma determinada ordem
- Podem ter valores heterogêneos( vários tipos de valores dentro de um mesmo dicionário: inteiros, strings, listas, etc)
- Chaves são únicas obrigatoriamente
- Mais intuitivos de trabalhar
'''

mais_vendidos = {
    'tecnologia': 'iphone',
    'refrigeração':'ae consul 12000 btu',
    'livros':'o alquimista',
    'eletrodomestico':'geladeira'
    }

vendas_tecnologia = {
    'iphone': 1500,
    'samsung galaxy':12000,
    'tv samsung':10000,
    'ps5':14300,
    'tablet':1720
    }

livro = mais_vendidos['livros']
eletrodomestico = mais_vendidos['eletrodomestico']
print(livro)
print(eletrodomestico)
qtd_ps5 = vendas_tecnologia['ps5']
qtd_tablet = vendas_tecnologia['tablet']
print(qtd_ps5)
print(qtd_tablet)