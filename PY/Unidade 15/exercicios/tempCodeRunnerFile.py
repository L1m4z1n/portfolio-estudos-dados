import numpy as np

quantidade = np.array([5,3,2])
precos = np.array([100,200,50])

total_vendas = np.dot(quantidade,precos)
print(total_vendas)