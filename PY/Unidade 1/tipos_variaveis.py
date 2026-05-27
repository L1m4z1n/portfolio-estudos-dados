'''
Uma variável é um objeto, afinal tudo é um objeto em Python

int -> inteiro
string -> texto
float-> números com casas decimais(ponto flutuante)
bool ou bollean -> True ou False

Obs: Variáveis em Python não são declaradas explicitamente, mas isso não significa que você deve ficar mudando o tempo todo

Obs2: Cuidado com os nomes restritos(arquivo para Download)
'''

faturamento = 1000
print(type(faturamento)) # Int

faturamento = 1000.00
print(type(faturamento)) # Float

faturamento = '1.000'
print(type(faturamento)) # String

ganha_bonus = True
print(type(ganha_bonus)) # Bollean

'''
Tudo isso retorna:
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
'''