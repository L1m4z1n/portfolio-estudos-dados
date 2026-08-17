'''
1. Tirando informações de listas e dicionários

Digamos que você está analisando as vendas de produtos de uma empresa de varejo.

Essa lista tem: (produto, vendas de 2019, vendas de 2020) para cada produto.

Crie uma lista com as vendas de 2019.
'''

vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

lista_vendas2019 = []

for produto, vendas2019, vendas2020 in vendas_produtos:
    lista_vendas2019.append(vendas2019)
print(lista_vendas2019)


lista_vendas2019_2 = [vendas2019 for produto, vendas2019, vendas2020 in vendas_produtos]
print(lista_vendas2019_2)

# Qual é o maior valor de 2019?
print(max(lista_vendas2019_2))

# Qaul produto vendeu mais em 2019?

lista_vendasprodutos2019_2 = [(vendas2019,produto) for produto, vendas2019, vendas2020 in vendas_produtos]
print(max(lista_vendasprodutos2019_2))