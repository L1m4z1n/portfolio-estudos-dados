'''
## Exercício 1

Você é um gerente de vendas e tem os dados de vendas de um produto para os últimos 7 dias em uma lista: `[127, 90, 201, 150, 210, 220, 115]`. Calcule a média de vendas durante a semana.
'''

import numpy as np

dados = [127, 90, 201, 150, 210, 220, 115]

vendas = np.array(dados)
media_vendas = np.mean(vendas)
print(f"A média de vendas durante a semana foi de {media_vendas} unidades por dia.")

'''
## Exercício 2

Você é um analista financeiro e tem os preços de fechamento diário de uma ação para a última semana em um array NumPy: `precos = np.array([31.40, 31.25, 30.95, 31.20, 31.60, 31.50])`. Calcule o preço máximo, mínimo e a variação de preço durante a semana.
'''
import numpy as np
precos = np.array([31.40, 31.25, 30.95, 31.20, 31.60, 31.50])
preco_maximo = np.max(precos)
preco_minimo = np.min(precos)
variacao = preco_maximo - preco_minimo
print(f'O preço máximo é igual a: {preco_maximo}\nO preço minimo é igual a: {preco_minimo}\nA variação é igual a: {variacao}')


'''
## Exercício 3

Sua loja vendeu em um dia 5 unidades do *Produto A*, 3 unidades do *Produto B* e 2 unidades do *Produto C*. Os preços dos produtos são, respectivamente, 100, 200 e 50 reais. Calcule o total de vendas do dia.
'''

import numpy as np

quantidade = np.array([5,3,2])
precos = np.array([100,200,50])

total_vendas = np.dot(quantidade,precos)
print(total_vendas)