produtos = ['apple tv', 'mac', 'IPhone x', 'IPhone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
produtos.sort()
print(produtos)

# Como fariamos para ordenar corretamente?
produtos.sort(key=str.casefold)
print(produtos)
