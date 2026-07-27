'''
Retornar um valor na function python

Estrutura básica

def nome_funcao():
    return valor_final

Ex:. Vamos criar uma função de cadastro de um produto. essa função deve garantir que o produto cadastrado está em letra minúscula
'''

def cadastrar_produto():
    produto = input('Digite o nome do produto que deseja cadastrar: ')
    produto = produto.casefold()
    produto = produto.strip()
    return produto

for i, j in enumerate(range(5)):
    variavel_produto = cadastrar_produto()
    i+= 1
    print(f"Produto {i}: {variavel_produto} cadastrado com sucesso!!")
