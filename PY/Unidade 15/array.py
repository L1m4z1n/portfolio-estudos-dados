'''
Array
Um array é uma estrutura de dados que armazena valores do mesmo tipo. Em Python, isso é uma grande vantagem proque economiza espaço e permite operações mais eficientes. Vamos criar um array.
'''
import numpy as np

#criação de um array
array = np.array(["a","b","c","d","e"])
print(array)

#Conhecendo um array: indexação e slice

print(array[4])
# e
print(array[1:4])
# 'b','c','d'
print(array[0:-1])
# 'a','b','c','d'
print(array[0:-1:2])
# 'a','c'
print(array[0::2])
# 'a','c','e'
print(array[::2])
# 'a','c','e'
print(array[: : 3])
# 'a','d'
print(array[:])
# 'a','b','c','d','e'
print(array[::-1])
# 'e','d','c','b','a'