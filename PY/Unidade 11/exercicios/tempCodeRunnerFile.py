from datetime import datetime, date
import locale
locale.setlocale(locale.LC_TIME,"pt_BR")

# Pegando a data atual
dia_hoje = date.today()
print(dia_hoje)

# Obtendo informações das últimas transações
dia = int(input("Dia da última transação: "))
mes = int(input("Mês da última transação: "))
ano = int(input("Ano da última transação: "))

# Organizando as datas
data_organizada = date(ano,mes,dia)

# Formato string
data_formatada = data_organizada.strftime("%d de %B de %Y")

tempo_transacao = dia_hoje - data_organizada 

if tempo_transacao.days >= 30:
    print("Você obteve desconto")
else:
    print("Em dia")