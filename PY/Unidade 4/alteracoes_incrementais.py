"""
Alterações "Incrementais" de Variaáveis

Estrutura:
 - variavel = variavel + outro_valor

ou então
 - variavel += outro_valor

 Exemplo: vamos adicionar às variáveis criadas o Produto Ipad, 500 vendas
"""

faturamento = 3000

faturamento = faturamento + 1000 #4000

lista = ['mac','iphone']
vendas = [100,200]

#adicionando ipad na lista

lista = lista + ['ipad']
print(lista)

soma_vendas = 300
#adicionando na soma a quantidade de Ipad

soma_vendas = soma_vendas + 500
print(soma_vendas)