'''
 Juntar listas, ordenar e cuidados especiais
2 formas:

lista1.extend(lista2)
lista_nova = lista1 + lista2

 Obs: O metodo .append não junta listas, mas adiciona um valor
 
'''
produtos = ['apple tv','mac','iphone x','ipad','apple watch']
novos_produtos = ['iphone 12', 'ioculos']

produtos.extend(novos_produtos)
print(produtos)

todos_produtos = produtos + novos_produtos
print(todos_produtos)

#Cuidado
# [1] [2] não é a mesma coisa que 1 + 2, então cuidado sempre com o formato dos valores na hora de fazer operações

vendas = [1000,1500,15000, 20000, 270]
vendas_iphonex = [15000]
vendas_iphone11 = [20000]

total_iphone = vendas[2] + vendas [1]
total_iphone_listas = vendas_iphonex + vendas_iphone11
print(total_iphone_listas)
print(total_iphone)

# Ordenar Listas
vendas.sort(reverse=True) # Se reverse for igual a True ela imprime lista reversa se for false lista normal
print(vendas)
