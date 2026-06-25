produtos = ["celular", "camera", "fone de ouvido", "monitor"]
precos = [1500, 1000, 800, 2000]

nome_produto = input("Nome do produto:")

if nome_produto in produtos:
    i_produto = produtos.index(nome_produto)
    txt_produto = produtos[i_produto]
    preco_produto = precos[i_produto]
    print(f'O produto {txt_produto} custa R${preco_produto}')
else:
    print('Produto inexistente, tente novamente!!!')