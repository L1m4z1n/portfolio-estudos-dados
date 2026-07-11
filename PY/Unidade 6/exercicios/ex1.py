# Input até o usuário parar

vendas = [
    ['maçã', 5],
    ['banana', 15],
    ['azeite', 1],
    ['vinho', 3],
]


while True:
    add_produtos = input("Digite o produto a ser adicionado:")
    if not add_produtos:
        break
    qtd_produto = int(input(f"Qual a quantidade de {add_produtos} será adicionado:"))
    vendas.append([add_produtos,qtd_produto])
print(vendas)