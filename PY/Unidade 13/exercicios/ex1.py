'''
Um exemplo prático de List Comprehension

O que fariamos se quisermos ordenar 2 listas "relacionadas"
'''

vendas_produtos = [1500,150,2100,1950]
produtos = ['vinhos','cafeiteira','microondas','iphone']

lista_auxiliar = list(zip(vendas_produtos,produtos))
lista_auxiliar.sort()

produtos = [produto for vendas, produto in lista_auxiliar]
print(produtos)