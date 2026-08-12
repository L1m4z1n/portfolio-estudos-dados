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