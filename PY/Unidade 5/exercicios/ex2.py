'''# Exercícios

## 1. Calculando % de uma lista

Faremos algo parecido com "filtrar" uma lista. Mais pra frente no curso aprenderemos outras formas de fazer isso, mas com o nosso conhecimentoa atual já conseguimos resolver o desafio.

Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, eu quero conseguir calcular o % de vendedores que bateram a meta. Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.'''

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

vendedor_meta = []

for i,vendedor in enumerate(vendas):
    if vendedor[1] >= meta:
        vendedor_meta.append(vendedor)
        porcent = (len(vendedor_meta)/len(vendas))
        melhor_vendedor = max(vendedor_meta)
print(f'{vendedor_meta}\n{porcent:.1%}\n{melhor_vendedor}')
#seu código aqui