import numpy as np
rng = np.random.default_rng(seed=42)
dados_vendas = rng.integers(low=50, high=200, size=30)
print(dados_vendas)

#[ 63 166 148 115 114 178  62 154  80  64 128 196 160 164 157 167 126  69
# 175 117 125 105  77 189 167 146 110 173 131 116]

'''
Agora, você pode usar esses dados para realizar várias análises. Por exemplo, você pode querer saber qual foi o dia com as vendas mais altas, as vendas mais baixas, ou a média de vendas durante o mês. Aqui está como você pode fazer isso:
'''
print(np.max(dados_vendas))

print(np.argmax(dados_vendas)+1)

print(np.mean(dados_vendas))