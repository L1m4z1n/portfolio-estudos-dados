"""
Exemplo real com condicional(Importância da identação)
"""

meta_vendas = 50000
qtd_vendas = 65300

if qtd_vendas >= meta_vendas:
    print(f"Batemos a meta de vendas de Iphone, vendemos {qtd_vendas} unidades")
else:
    print(f"Infelizmente não batemos a meta, vendemos {qtd_vendas} unidades. A meta era {meta_vendas} unidades")


"""
Blocos e Identação
Devemos sempre usar a identação para dizer para o programa onde a estrutura começa e onde ela termina.

Exemplo do Video 2 de IF
"""
meta = 0.05
taxa = 0
rendimento = 0.10

if rendimento > meta:
    taxa = 0.02
    print(f"Taxa de {taxa}")
else:
    taxa = 0
    print(f"A taxa foi de {taxa}")