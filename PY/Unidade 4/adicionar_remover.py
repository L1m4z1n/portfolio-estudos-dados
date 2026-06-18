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

# 2 FORMAS DE TRATAR O ERROR

# 1 - Criar um IF para evitar que ele aconteça
# 2 - Esperar que ele possa acontecer e tratar caso o erro aconteça com:
#try:
    #tenta fazer
#except:
    #caso de errado

try:
    produtos.remove('iphonex')
    print(produtos)
except:
    print('Produto não existe')