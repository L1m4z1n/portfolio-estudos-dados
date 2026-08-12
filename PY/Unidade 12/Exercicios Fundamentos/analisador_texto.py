'''
Crie um programa que analise um texto fornecido pelo usuário. O programa deve contar o número de palavras (independentemente se há repetição ou não), a quantidade de cada palavra e a quantidade de cada letra. Ignore maiúsculas e minúsculas ao contar letras (ou seja, transforme tudo para minúsculas). Faça o devido tratamento para pontuação e espaços ao contar palavras.

O programa deve conter uma função chamada `analisar_texto` que recebe o texto como parâmetro e retorna a contagem de palavras, a frequência de palavras e a frequência de letras. A função deve ser devidamente documentada.

Para o texto "Olá mundo! Este é um teste. Olá novamente." o programa deve imprimir:

```
Contagem de palavras: 8
Frequência de palavras: Counter({'Olá': 2, 'mundo': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste': 1, 'novamente': 1})
Frequência de letras: Counter({' ': 7, 'e': 6, 'o': 4, 't': 4, 'm': 3, 'n': 3, 'l': 2, 'á': 2, 'u': 2, 's': 2, 'd': 1, 'é': 1, 'v': 1, 'a': 1})
```

Dica: use o módulo `string` para obter uma lista de caracteres de pontuação. Exemplo:
'''
import string
print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz

print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.digits)
# 0123456789


#Dica: use o módulo `collections` para obter um contador de palavras e letras. Exemplo:
import string
from collections import Counter
#print(Counter(['a', 'b', 'a', 'c', 'b', 'a']))
#print(Counter('abacba'))


# Solução Simples

def analisar_texto(texto):

    """
    Analisa o texto fornecido e calcula a contagem de palavras, a frequencia de palavras 
    e frequência de letras.

    Parameters
    ----------
    texto: str
        texto a ser analisado

    returns:
    ----------
    tuple
        Contagem de palacras, frequência de palavras, frequência de letras
    
    """

    tratamento = str.maketrans("","", string.punctuation)
    texto_tratado = texto.translate(tratamento)
    palavras = texto.split()
    contagem_palavras = len(palavras)
    frequencia_palavras = Counter(palavras)
    frequencia_letras = Counter(texto_tratado.lower())
    return contagem_palavras, frequencia_palavras, frequencia_letras

texto = "Olá mundo! Este é um teste. Olá novamente."
contagem_palavras, frequencia_palavras, frequencia_letras = analisar_texto(texto)

print(f"Contagem de palavras: {contagem_palavras}")
print(f"Frequência de palavras: {frequencia_palavras}")
print(f"Frequência de letras: {frequencia_letras}")