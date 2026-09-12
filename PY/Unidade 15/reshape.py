'''
# Guia de Introdução ao NumPy

NumPy, que significa Numerical Python, é uma biblioteca fundamental para a computação científica em Python. Ela fornece suporte para arrays e matrizes, além de funções matemáticas para operações com esses objetos. É, também, a base da biblioteca Pandas.


## np.reshape()

A função `reshape()` é usada para alterar a forma de um array. Por exemplo, se você tem dados de vendas para 2 semanas e quer reorganizá-los em uma matriz de 2x7 (2 semanas, 7 dias por semana).

'''
import numpy as np

# Vendas diárias para 2 semanas
vendas = np.array([200, 220, 250, 210, 300, 280, 230, 210, 220, 240, 230, 210, 280, 220])

# Reorganizar os dados em uma matriz de 2x7
vendas_reshaped = np.reshape(vendas, (2, 7))
print(vendas_reshaped)

print(vendas_reshaped.ndim)# Numero de direções

print(vendas_reshaped.shape)#Comprimento/forma

# DOM SEG TER QUA QUI SEX SAB

print(vendas_reshaped.sum(axis=0))

# Exemplo
'''
Considere que uma loja funciona de segunda a sábado, independentemente de feriados. Nos últimos 30 dias, teve o menor volume de vendas sendo 20 e o maior sendo 200. Crie uma simulação das vendas desses últimos 30 dias, separando por semanas. Calcule:
- o total de vendas por semana
- a média de vendas por semana
- a média de vendas por dia da semana

'''
import numpy as np
rng = np.random.default_rng(seed=42)
vendas = rng.integers(low=20,high=200,size=30,endpoint=True)
print(vendas)
# Pelo enunciado, o padrão de dias é:
# seg, ter, qua, qui, sex, sab, seg, ter, qua, qui, sex, sab, ...
vendas_semanais = np.reshape(vendas,(-1,6))
print(vendas_semanais)