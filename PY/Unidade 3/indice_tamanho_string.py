# 0 1 2 3 4 5 6 7 8 9 10 11 12 13
# l i r a @ g m a i l  .  c  o  m 

# Pegar um item de uma string: texto[índice] 

email = 'lira@gmail.com'
nome = 'João Lira'

# len: conta a quantidade de caracteres
print(len(email))

# detalha posição da string
print(email[4] )

# Indice Negativo

# -14  -13  -12  -11  -10 -9 -8  -7  -6   -5   -4   -3   -2   -1
# l     i    r   a    @   g   m  a   i    l    .    c    o    m 

#pedaço de um texto
print(email[:2])
#Dois pontos antes se quiser antes do indice escolhido e dois pontos depois se quiser depois do indice escolhido

#exercicio
print(f'Tamanho do e-mail: {str(len(email))} caracteres')
print(f'Primeiro Caractere: {email[0]}')
print(f'Último Caractere: {email[-1]}')
