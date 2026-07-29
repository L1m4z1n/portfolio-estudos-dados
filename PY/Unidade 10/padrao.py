'''
# Valores Padrões para os argumentos

### Estrutura

- Nesse caso, você não é obrigado a passar o valor para usar a função, pode usar o valor padrão.

def minha_funcao(argumento = valor_padrao):
    ...
    return ...

- Como vimos, o sort() para listas tem um argumento padrão. O reverse = False é padrão, então a ordem é crescente. Caso o usuário queira fazer em ordem decrescente, o reverse deve ser alterado para True
'''


produtos = ['apple tv', 'mac', 'iphone x', 'iPad', 'apple watch', 'mac book', 'airpods']

produtos.sort()
print(produtos)

produtos.sort(reverse = True)
print(produtos)

'''
- Vamos criar uma função que padronize códigos de produtos. O default será padronizar os códigos para letras minúsculas (dado por 'm'), mas se o usuário quiser pode padronizar para maiúscula, dado por ('M').
'''

def padronizar_codigos(lista_codigos, padrao='m'):
    for i, item in enumerate(lista_codigos):
        item = item.replace('  ', ' ')
        item = item.strip()
        if padrao == 'm':
            item = item.casefold()
        elif padrao == 'M':
            item = item.upper()
        lista_codigos[i] = item
    return lista_codigos


cod_produtos = [' ABC12 ', 'abc34', 'AbC37']
print(padronizar_codigos(cod_produtos))