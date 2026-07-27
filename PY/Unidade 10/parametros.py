'''
Argumentos/Parâmetros da função

Estrutura:
def minha_funcao(parametro1,paramentro2,parametro3):
    return parametro1+parametro2+parametro3

Exemplo nossa famoso print
'''

def minha_soma(num1,num2,num3):
    return num1 + num2 + num3

soma = minha_soma(10,20,30)
print(soma)


'''
Vamos criar uma function com parâmetro
Digamos que estamos criando um programa para categorizar os produtos de uma revendedora de bebidas.

Cada produto tem um código. O tipo de produto é dado pelas 3 primeiras letras do código.

Ex:
Vinho -> BEB12302
Cerveja -> BEB12043
Vodka -> BEB34501

Guaraná -> BSA11104
Coca -> BSA54301
Sprite -> BSA34012
Água -> BSA09871

Repare que bebidas não alcóolicas começam com BSA e bebidas alcoolicas começam com BEB.

Crie um programa que analise uma lista de produtos e envie instruções para a equipe de estoque dizendo quais produtos devem ser enviados para a área de bebidas alcóolicas.
'''

def ehalcoolico(bebida):
    bebida = bebida.upper()
    if 'BEB' in bebida:
        return True
    else:
        return False

produtos = ['beb46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

#percorrer toda a lista de produtos
#pra cada produto, verificar se ele é bebida alcoolica
#se for bebida alcoolicaa, exibir mensagem enviar...

for produto in produtos:
    if ehalcoolico(produto):
        print(f"Enviar {produto} para setor de bebidas alcoolicas")