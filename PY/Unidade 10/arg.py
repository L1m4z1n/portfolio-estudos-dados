'''
Quantidades indefinidas de Argumentos

Utilidade:
Quando você quer permitir uma quantidade indefinida de argumentos , usa o * para isso

Estrutura:

*args ara positional arguments -> argumentos vêm em formato de tupla

def minha_funcao(*args):
    ...

**kwargs para keyword arguments -> argumentos vêm em formato de dicionario

 def minha_funcao(**kwargs):
    ...

'''

def minha_soma(*numeros):
    soma = 0
    for numero in numeros:
        soma+= numero
    return soma

print(minha_soma(10,20,30,40))

def preco_final(preco, **adicionais):
    #print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1-adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra']
    if 'imposto' in adicionais:
        preco *= (1+ adicionais['imposto'])
    return preco

print(preco_final(1000, desconto=0.1,garantia_extra = 100, imposto=0.3))