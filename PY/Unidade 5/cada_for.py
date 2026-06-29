produtos = ["iphone", "ipad", "airpod", "macbook"]
precos = [7000,1000,2500,14000]

# For item in lista

# preco com imposto

for preco in precos:
    print(preco * 1.1)

# For i in range

# preco de cada produto
for i in range(len(precos)):
    produto = produtos[i]
    preco = precos[i]
    print(produto,preco)

# For item in lista com enumerate

# preco de cada produto com imposto

for i,preco in enumerate(precos):
    i += 1
    produto = produtos[i]
    print(f"{i}: {preco * 1.1}")