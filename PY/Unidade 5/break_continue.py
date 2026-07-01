#Formas de interromper um for

'''
2 opções: 

break -> interrompe e finaliza o for
continue -> interrompe e vai para o próximo item do for
'''

vendas = [100,150,1500,2000,120]

# caso 1: se todas as vendas forem acima da meta, a loja ganha bonus

meta = 110

for venda in vendas:
    if venda < meta:
        print('A loja não ganha bonus')
        break
    print(venda)

# caso 2: exiba quem bateu a meta

vendedores = ['João', 'Julia', 'Ana', 'José', 'Maria']
meta = 130

for venda in vendas:
    if venda < meta:
        continue
    print(venda)