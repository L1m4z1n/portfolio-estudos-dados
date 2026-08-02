'''
Docstring e Annotations

Estrutura - são ferramentas "apenas" para organização:

Quando criamos uma função, normalmente não seremos as únicas pessoas a usarem essa função e também pode ser que a gente precise usar essa mesma função semanas, meses ou até anos depois da sua criação.

- Docstring -> diz o que a função faz, quais valores ela tem como argumento e o que significa cada valor
- Annotation -> diz o que devem ser os argumentos e o que a função retorna

Em muitas empresas, o time de tecnologia vai ter um padrão que você deve seguir para isso, mas caso não tenha, vamos te mostrar um padrão bom a ser utilizado.

Docstring:

def minha_funcao(arg1,arg2,...):
        O que a função faz

    Parameters:
        arg1 (int): O que é o argumento 1
        arg2 (str): O que é o argumento 2

    Returns:
        texto (str): o que a função retorna com resposta

    ...código da função

'''

def minha_soma(num1,num2,num3):
    '''
    Faz a soma de 3 números inteiros e devolve como resposta um inteiro

    Parameters:
    num1(int): primeiro número a ser somado
    num2(int): segundo número a ser somado
    num3(int): terceiro número a ser somado

    Returns:
        Soma(int): o valor da soma dos 3 números dados como argumento

    '''
    return num1 + num2 + num3

minha_soma()


# Annotation:

'''
def minha_funcao(arg1: isso, arg2: aquilo) -> o que a função retorna:

...
return ...
'''

def minha_funcao(num1: 'primeiro número a ser somado', num2: int, num3: int) -> int:
    """
    Soma três números inteiros.

    Args:
        num1 (int): primeiro número a ser somado
        num2 (int): segundo número
        num3 (int): terceiro número

    Returns:
        int: resultado da soma
    """
    return num1+num2+num3
