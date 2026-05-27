# Forma errada de se concatenar, pois você está tentando concatenar um texto com um número inteiro.
# Solução: Transforma número inteiro em String
#faturamento = 1000
#print('O faturamento da loja foi ' + faturamento)

# Solução
faturamento = 1000
print('O faturamento da loja foi ' + str(faturamento))

#Outros exemplos
faturamento = 1500
custo = 500
lucro = faturamento - custo

print('O faturamento da loja foi ' + str(faturamento))
print('O custo da loja foi ' + str(lucro) + ' reais')