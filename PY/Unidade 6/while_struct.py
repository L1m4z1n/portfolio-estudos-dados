'''
Estrutura While
Usamos o while quando queremos repetir um código de forma indeterminada até uma condição se tornar verdadeira/falsa.

while condição:
repete esse código

'''

venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia')
vendas = []

while venda != '':
    vendas.append(venda)
    venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter com a caixa vazia')
print(f'Registro Finalizado. Os produtos cadastrados foram: {vendas}')