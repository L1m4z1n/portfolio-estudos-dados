'''
sort (ou sorted) com function
Descrição:
Até agora no programa, usamos várias vezes o .sort() para ordenar listas

Mas o método sort tem um parâmetro que nunca usamos e que agora sabemos usar.
'''

produtos = ['apple tv', 'mac', 'IPhone x', 'IPhone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
produtos.sort()
print(produtos)

# Como fariamos para ordenar corretamente?
produtos.sort(key=str.casefold)
print(produtos)

# Como ordenar um dicionario de acordo com o valor
vendas_produtos = {'vinho': 100, 'cafeiteira': 150, 'microondas': 300, 'iphone': 5500}

# Queremos listar da maior quantidade de vendas para a menor, para enviar como report para o diretor, por exemplo

def segundo_item(tupla):
    return tupla[1]
lista_vendas = list(vendas_produtos.items())
lista_vendas.sort(key=segundo_item, reverse=True)
print(lista_vendas)