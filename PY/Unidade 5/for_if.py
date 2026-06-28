'''
for item in lista:
    if condicao:
        faça alguma coisa
    else:
        outra coisa
'''

vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
meta = 1000

qtd_meta = 0

for venda in vendas:
    if venda >= meta:
        qtd_meta +=1
        qtd_funcionarios = len(vendas)
        porcent_meta_batida = qtd_meta/qtd_funcionarios
        print(f'{qtd_meta}: {venda}\nPorcentagem de meta batida: {porcent_meta_batida:.1%}')