custo = 500
faturamento = input('Qual foi o faturamento da loja no dia de hoje: ')

try:
    lucro = int(faturamento) - int(custo)
    print(lucro, int('lucro 500'))
except ValueError:
    print('Coloque apenas o valor do faturamento, sem texto nenhum, apenas números')