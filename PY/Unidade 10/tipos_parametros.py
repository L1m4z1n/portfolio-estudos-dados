'''
Mais de 1 argumento e formas de passar argumento para uma função

Estrutura:

- 2 formas de passar o argumento:
    1. Em ordem (positional argument)
    2. Com o nome do argumento (keyword argument)

- Vamos mudar a função que fizemos na aula passada para conseguir categorizar qualquer tipo de bebida de acordo com o "rótulo" passado para a nsosa function. Basicamente nossa function agora tem que verificar se o produto é da categoria passada ou não.
'''

def eha_da_categoria(bebida, cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        return False


produtos = ['CAR46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

for produto in produtos:
    if eha_da_categoria(produto,'BEB'):
        print('Enviar {} para setor de bebidas alcóolicas'.format(produto))
    elif eha_da_categoria(produto,'BSA'):
        print('Enviar {} para setor de bebidas não alcóolicas'.format(produto))
## Obs Importante: Sua função deve estar SEMPRE antes de ser usada.

##- Normalmente, nos nossos códigos, fazemos as definições de todas as funções antes e depois construimos o resto do código.
##- É comum dar '2 enters' após a definição da função para deixar o código mais organizado
