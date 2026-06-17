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