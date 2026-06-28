# Estrutura de repetição: For

# for i in range(n):
#   repetir código n vezes

for i in range(5):
    print('lira')

produtos = ['coca','pepsi','guarana','sprite','fanta']
producao = [15000,12000,13000,5000,250]

tamanho = len(produtos)

for i in range(tamanho):
    print(f'{producao[i]} unidades produzidas de {produtos[i]}')