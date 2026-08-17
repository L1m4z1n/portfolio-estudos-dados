meta = 1000
vendas_produtos = [1500,150,2100,1950]
produtos = ['vinho', 'cafeiteira','microondas','iphone']

produtos_acima_meta = [produto for i, produto in enumerate(produtos) if vendas_produtos[i] > meta]
print(produtos_acima_meta)