'''
# Exercícios

## 1. Faturamento do Melhor e do Pior Mês do Ano

Qual foi o valor de vendas do melhor mês do Ano?
E valor do pior mês do ano?
'''
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas = vendas_1sem + vendas_2sem
melhor_valor = max(vendas)
pior_valor = min(vendas)

melhor_mes = meses[vendas.index(melhor_valor)]
pior_mes = meses[vendas.index(pior_valor)]

print(f"{melhor_mes} foi o melhor mês, com faturamento de {melhor_valor}")

'''
## 2. Continuação

Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.

Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.

Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista
'''
faturamento_total = sum(vendas)
print(f"{faturamento_total} é o faturamento total!")

'''
## 3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")

Dica: o método remove retira um item da lista.
'''
top_3_valores = sorted(vendas, reverse=True)[:3]
top_3 = [(meses[vendas.index(valor)], valor) for valor in top_3_valores]

print("Top 3 meses de vendas:")
for mes, valor in top_3:
    print(f"{mes}: {valor}")
