'''
Exceções e Erros em Funções

Como "testar" erros e tratar exceções:

try: 
    o que eu quero tentar fazer
except:
    o que vou fazer caso de erro

'''

def descobrir_servidor(email):
    try:
        posicao_a = email.index('@')
        servidor = email[posicao_a:]
        if 'gmail' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        elif 'uol' in servidor or 'bol' in servidor:
            return 'uol'
        else:
            return 'não determinado'
    except:
        raise Exception('Email digitado não tem @, digite novamente')
    
email = input('Qual é o seu e-mail: ')
print(descobrir_servidor(email))

# Cuidado uma vez dentro do try. Qualquer erro vai levar para o except

'''
Como "printar" um erro em uma function

raise Exception('O erro foi esse')

ou então avisando qual o tipo de erro que ele teve

raise TypeError('O erro foi esse')
raise ValueError('O erro foi esse')
raise ZeroDivisionError('O erro foi esse')


'''

'''
Tratamento Completo:

try:
    tente fazer isso
except ErroEspecifico:
    deu esse erro aqui que era superado
else:
    caso não dê o erro esperado, rode isso.
finally:
    independente do que acontecer, faça isso.


'''

#passo 1 -> mostrar o erro de faturamento - custo se a pessoa digitar texto.
#passo 2 -> colocar um except para tratar o ValueError
#passo 4 -> usar um else para exibir o print(lucro) e mostrar a diferença que seria de colocar o print(lucro dentro
# caso o print(lucro levantasse um ValueError, ele ia pular pro except também), então muitas vezes é melhor isolar

custo = 500
faturamento = input('Qual foi o faturamento da loja no dia de hoje: ')

try:
    lucro = int(faturamento) - int(custo)
    print(lucro, int('lucro 500'))
except ValueError:
    print('Coloque apenas o valor do faturamento, sem texto nenhum, apenas números')
    