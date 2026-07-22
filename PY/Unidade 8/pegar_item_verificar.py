'''
Não confie na ordem dos dicionarios, use as chaves

'''

mais_vendidos = {
    'tecnologia': 'iphone',
    'refrigeração':'ae consul 12000 btu',
    'livros':'o alquimista',
    'eletrodomestico':'geladeira'
    }

vendas_tecnologia = {
    'iphone': 1500,
    'samsung galaxy':12000,
    'tv samsung':10000,
    'ps5':14300,
    'tablet':1720
    }

# duas formas de pegar um valor:
#- dicionario[chave]
#- .get(chave)


#respondendo com a chave
print(mais_vendidos['livros'])

#respondendo com o método get
print(vendas_tecnologia.get('iphone'))

'''
Verificar se item está no dicionário:
- if
- .get(chave) = none
'''

if vendas_tecnologia.get('copo') == None: 
    print('Copo não está dentro da lista de produtos de tecnologia')
else:
    print(vendas_tecnologia.get('copo'))