'''
Operações com String
str -> Transforma número em String
in -> Verifica se um texto está contido dentro de outro
operador + -> concatenar string
format e {} -> substitui valores
%s -> substitui textos
%d -> substitui números decimais
'''

faturamento = 1000
custo = 500
lucro = faturamento - custo

print(f'O faturamento da loja foi de:{faturamento}, o custo foi de {custo}, e o lucro de {lucro}')

#Uso de %s e %d
print(f'O faturamento foi de: %d. o custo de %d e o lucro de %d' % (faturamento,custo,lucro))

#Uso do In
print('@' in 'lira@gmail.com')
print('@' in 'lira.gmail.com')