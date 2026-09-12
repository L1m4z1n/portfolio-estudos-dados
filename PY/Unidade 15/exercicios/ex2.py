'''
## Exercício

Você é um analista de RH e tem os salários de todos os funcionários da sua empresa em um array NumPy. Seu trabalho é identificar quantos funcionários ganham acima da média. Use o seguinte array para sua análise: `salarios = np.array([3000, 2500, 3500, 4000, 2000, 4500, 3000, 3800, 4800])`.
'''

import numpy as np

salarios = np.array([3000, 2500, 3500, 4000, 2000, 4500, 3000, 3800, 4800])

media_salario = np.mean(salarios)
funcionarios_acima_media = np.sum(salarios>media_salario)

print(funcionarios_acima_media)


# OUtra forma

print(np.count_nonzero(salarios > media_salario))