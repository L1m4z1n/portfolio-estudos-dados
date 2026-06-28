'''
For "each"

O for no Python consegue percorrer uma lista e a cada "loop" retornar p valor do item.

for i in range(5):
    print(i)

range(5) é na verdade uma lista do tipo: [0, 1, 2, 3, 4]

Usando para listas:

for item in lista:
    print(item)

ou então para string

for ch in texto:
    print(ch)
'''

produtos = ['coca','pepsi','guarana','sprite','fanta']
texto = 'lira@gmail.com'


for i in range(5):
    print(f'O produto é {produtos[i]}')

for ch in texto:
    print(ch)