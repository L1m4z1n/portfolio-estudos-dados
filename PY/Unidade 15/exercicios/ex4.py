'''
## Exercício

Você é um gerente de vendas e tem os dados de vendas de três produtos diferentes (Produto A, Produto B, Produto C) para os últimos 5 dias em um array 2D NumPy. Cada linha do array representa um produto e cada coluna representa um dia. Seu trabalho é calcular as vendas totais para cada produto e para cada dia.

Use o seguinte array para sua análise:

```python
vendas = np.array([[50, 60, 70, 65, 80],
                   [85, 90, 78, 92, 88],
                   [72, 75, 68, 77, 76]])
```

**Solução:**
'''
import numpy as np

vendas = np.array([[50, 60, 70, 65, 80],
                   [85, 90, 78, 92, 88],
                   [72, 75, 68, 77, 76]])

vendas_reshaped = np.reshape(vendas,(3,5))

venda_semana = (vendas_reshaped.sum(axis=1))

venda_dia = (vendas_reshaped.sum(axis=0))

for i,venda in enumerate(venda_semana,start=1):
    print(f"Produto {i}: {venda}")   

for j, venda_diaria in enumerate(venda_dia,start=1):
    print(f"Venda do dia {j}: {venda_diaria}") 
    
