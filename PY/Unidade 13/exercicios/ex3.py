'''
List comprehensions com if para "filtrar" itens

Estrutura:
lista = [expressao for item in iterable if condicao]

Digamos que eu queira criar uma lista de produtos que bateram a meta

'''

meta = 1000
vendas_produtos = [1500,150,2100,1950]
produtos = ['vinho', 'cafeiteira','microondas','iphone']

# Fazendo por For tradicional

produtos_acima_meta = []

for i, produto in enumerate(produtos):
    if vendas_produtos[i] > meta:
        produtos_acima_meta.append(produto)
print(produtos_acima_meta)


# List comprehension
meta = 1000
vendas_produtos = [1500,150,2100,1950]
produtos = ['vinho', 'cafeiteira','microondas','iphone']

produtos_acima_meta = [produto for i, produto in enumerate(produtos) if vendas_produtos[i] > meta]
print(produtos_acima_meta)