'''
Enumerate permite que você percorra uma lista e ao mesmo tempo tenha em uma vriável o índice daquele item

for item in lista:
    resto do código

'''
funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']

for funcionario in funcionarios:
    print(funcionario)

# for i,item in enumerate(lista):
#    resto do código

funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']

for i,funcionario in enumerate(funcionarios):
    i+=1
    print(f"{i}: {funcionario}")

#Exemplo pratico

estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
nivel_minimo = 50

for i,qtd_estoque in enumerate(estoque):
    if qtd_estoque < nivel_minimo:
        print(f'{i}: {produtos[i]} está abaixo do nivel minimo. Temos apenas {qtd_estoque} unidades.')