'''
Adicionar e Remover itens de uma lista
'''

# Adicionar: lista.append(item)

# Remover: 
# item_removido = lista.pop(indice)
# lista.remove(item)

produtos = ['apple tv','mac','iphone x','ipad','apple watch']
# adicionar o iphone 11
produtos.append('Iphone 11')
print(produtos)
# remover iphone x
produtos.remove('iphone x')
item_removido = produtos.pop(2)
print(produtos)