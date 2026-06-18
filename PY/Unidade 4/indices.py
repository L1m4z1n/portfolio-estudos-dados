'''
Listas em Python
Estrutura:

lista = [valor,valor,valor,valor,...]

lista[i] -> é o valor de indice i da lista
Obs:. Lembre que no python o indice começa em 0, então primeiro item de uma lista é o item lista[0]

Para substituir um valor de uma lista vocÊ pode fazer:
lista[i] = novo_valor
'''

#Nesse caso as lista funcionam assim
produtos = ['TV','Celular','mouse','teclado','tablet']
#             0     1         2        3         4
vendas = [   1000, 1500,      350,    270,      900]

print(f'Vendas do produto {produtos[3]} foram de {vendas[3]}')


texto = 'gabriel@gmail.com'
print(texto[1])

# Como descobrir o índice de um item de uma lista
# i = lista.index('item')

produtos = ['TV','Celular','mouse','teclado','tablet']
estoque = [100,150,100,120,70,90,80]

i = produtos.index('Celular')
qtd_estoque = estoque[i]
print(f'Quantidade do {produtos[i]} em estoque é de {qtd_estoque}')

# Exercicio
produto = input("Digite o nome do produto:")
if produto in produtos:
    i = produtos.index(produto)
    qtd_estoque= estoque[i]
    print(f"Temos {qtd_estoque} unidades de {produto} no estoque")
else:
    print('Nome do produto não existe no estoque')