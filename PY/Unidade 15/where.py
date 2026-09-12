'''
# Guia de Introdução ao NumPy

NumPy, que significa Numerical Python, é uma biblioteca fundamental para a computação científica em Python. Ela fornece suporte para arrays e matrizes, além de funções matemáticas para operações com esses objetos. É, também, a base da biblioteca Pandas.

## Filtros e np.where()

A função `np.where()` é muito útil para fazer uma seleção condicional de elementos de um array. Por exemplo, em uma empresa, você pode querer identificar quais funcionários têm salários acima da média.
'''
import numpy as np

# Salários dos funcionários
salarios = np.array([3000, 3500, 4000, 2000, 4500, 4000, 5000])

# Calcular a média salarial
media_salarial = np.mean(salarios)

print(media_salarial)

# Identificar funcionários com salários acima da média
funcionarios_acima_media = np.where(salarios > media_salarial)
print(funcionarios_acima_media)
print(salarios[funcionarios_acima_media])
print(salarios[salarios > media_salarial])
print(np.where(salarios > media_salarial, "Acima da média", "Abaixo da média"))

# dar bônus de 10% para os funcionários com salários abaixo da média
salarios_bonus = np.where(salarios < media_salarial, salarios * 1.1, salarios)
print(salarios_bonus)

# filtrar os salários entre 3000 e 4500 com where

print(np.where((salarios>=3000) & (salarios <=4500)))

# filtrar os salários abaixo de 3000 ou acima de 4500 com where

print(np.where((salarios < 3000) | (salarios > 4500)))