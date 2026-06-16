'''
"Fórmulas" de Texto - Métodos de String
Estrutura:
Normalmente usamos a estrutura texto.método() para fazer as modificações que queremos
Alguns métodos pedem "argumentos", que são informações que temos que passar para a fórmula (método) para ela funcionar. Esses argumentos são passados dentro do parênteses
Como usar:
Não decore os métodos, os que você for mais usando com o tempo você vai decorar o que precisar.

Mas a dica é: use essa lista para consulta e busque entender como os métodos funcionam e suas aplicações, para poder consultar e usar quando precisar.

'''

# - capitalize() -> Coloca a 1ª letra Maiúscula
texto = 'lira'
print(texto.capitalize())

#- casefold() -> Transforma todas as letras em minúsculas (existe lower() mas o casefold é melhor normalmente)
texto = 'Lira'
print(texto.casefold())

#- count()	-> Quantidade de vezes que um valor aparece na string
texto = 'lira@yahoo.com.br'
print(texto.count('.'))

# - endswith() -> verifica se o texto termina com um valor especifico e da como resposta true or false
texto = 'lira@yahoo.com.br'
print(texto.endswith('gmail.com'))

# - find -> encontra a posição nas strings
texto = 'lira@yahoo.com.br'
print(texto.find('@'))

# - isalnum -> verifica se um número é todo feito por alfanuméricos(letras e números) -> letras cpm acento ou ç são consideradas letras para essa função
texto = 'João123'
print(texto.isalnum())

# isalpha -> verifica se um texto é todo feito de letras
texto = 'João'
print(texto.isalpha())

# isnumeric -> Verifica se um texto é todo feito de numeros
texto = '123'
print(texto.isnumeric())

# replace -> substitui um texto por outro texto em uma string
texto = '1000.0'
print(texto.replace('.',','))

# split -> separa uma string de acordo com um delimitador em vários textos diferentes
texto = 'lira@yahoo.com.br'
print(texto.split('@'))


#splitlines - > separa texto com varios textos de acordo com os 'entes'
texto = '''Olá, bom dia 
Venho por meio desse e-mail lhe informar o faturamento da loja no dia de hoje. 
Faturamento = R$2.500,00'''
print(texto.splitlines())


#title -> Coloca a 1º letra de casa palavra em maiscula
texto = 'joão paulo lira'
print(texto.title())

#upper -> coloca o texto todo em letra maiuscula
texto = 'beb123123'
print(texto.upper())