'''
Function Python

O que é?
As function são blocos de código que servem1 único propósito, fazem uma ação especifica.

Estrutura Básica

def nome_funcao():
    faça alguma coisa
    faça outra coisa
    return valor_final

- Exemplo: vamos criar uma função de cadastro de um produto. Essa função deve garantir que o produto cadastrado está em letra minúscula.
'''

def cadastrar_produto():
    produto = input("Digite o nome do produto que deseja cadastrar:")
    produto = produto.casefold()
    print(f"{produto} cadastrado com sucesso!")

for i in range(3):
    cadastrar_produto()