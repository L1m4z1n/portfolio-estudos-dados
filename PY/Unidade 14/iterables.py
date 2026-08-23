'''
Funcrion em iterables

Segue a mesma lógica de list comprehension, mas é mais simples

Basicamente alguns métodos e funções que já existem no python podem rodar uma function para cada item, da mesma forma ue fizemos com list comprehension.

Isso pode ajudar a gente a resolver alguns desafios de forma mais simples

Uma função que permite que a gente faça isso é a map function

map function
lista = list(map(função, iterable_original))

- Exemplo: digamos que eu tenha uma function que corrige um código de um produto(semelhante ao que fizemos na seção de function aqui do curso)
'''

def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace("  ", " ")
    texto = texto.strip()
    return texto

produtos = [' ABC12 ', 'abc34', 'AbC37', 'beb12', ' BSA151', 'BEB23']

#Usando o for
for i,produto in enumerate(produtos):
    produtos[i] = padronizar_texto(produto)
print(produtos)

# usando map
produtos = list(map(padronizar_texto, produtos))
print(produtos)