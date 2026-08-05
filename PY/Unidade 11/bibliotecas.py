'''
# O que são Módulos/Bibliotecas e qual a importância deles?

### Importância

- Já tem muita coisa pronta, então você não precisa criar do zero.
- Se você souber usar Bibliotecas e como usar uma bivblioteca nova, você vai conseguir fazer praticamente tudo no Python

### Estrutura Básica

import biblioteca

ou

import biblioteca as nome

- Exemplo: Como pode fazer o nosso código exibir a data e hora atual?
'''

import time as tm

print(tm.ctime())



### Variações

#importar a biblioteca sem precisar usar o nome dele
#from biblioteca import *

#importar apenas algumas partes da biblioteca
#from biblioteca import funcao1, funcao2, etc.

from time import *

print(ctime())

from time import ctime

print(ctime())