# Print de listas

# 2 opções:
# print "normal"
# método join -> texto.join(lista)

produtos = ['apple tv','mac','iphone x','ipad','apple watch']
print(produtos)
print('\n'.join(produtos))

# Lembrando do método split de strings:
# lista = texto.split(separador)
lista = produtos.split(', ')
print(lista)