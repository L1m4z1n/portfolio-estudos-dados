'''
List Comprehension
- é uma forma de iterar pelos elementos da lista de maneira "mais direta", com mais "cara de python"
- é como se vocÊ fizesse um "for" em 1 linha de código

Estrutura:
lista = [expressão for item in iterable

'''

preco_produtos = [100,150,300,5500]
produtos = ['vinho','cafeiteira','microondas','iphone']

#digamos que o imposto sobre os produtos é de 30%, ou seja, 0.3. Como eu faria para criar uma lista com os valores de imposto de cada produto?

preco_imposto = []

#usando o for

for precos in preco_produtos:
    preco_imposto.append(precos* 0.3)
print(preco_imposto)

# usando list comprehension

imposto = [preco * 0.3 for preco in preco_produtos]
print(imposto)

# A "expressão" na list comprehension pode ser uma function tambem

def calcular_imposto(preco,imposto):
    return preco * imposto

imposto = [calcular_imposto(preco, 0.3) for preco in preco_produtos]
print(imposto)