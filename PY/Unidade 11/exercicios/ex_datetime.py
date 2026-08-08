'''
## Oferecendo desconto para cliente com base na última compra

Suponha que você está trabalhando para uma empresa que deseja rastrear a atividade do cliente. Uma métrica que eles estão interessados é o tempo que passou desde a última transação do cliente. Se for muito tempo, eles podem oferecer um desconto para o cliente. Crie um script Python que mostra quanto tempo se passou desde a última compra do cliente. Se faz mais de 30 dias, mostre uma mensagem oferecendo um desconto para o cliente.

'''
# Descobrir quando foi a última transação do cliente importante ver o tempo atual
# Se for muito tempo, tem desconto. 30 dias como muito tempo
# Minha ideia é criar inputs perguntando dia, mês é ano, captar essas informações junta-las para formatar e calcular ou no caso tranformas em string e usar um strptime

from datetime import date
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
    print(f"Você obteve desconto, sua última transação foi no dia: {data_formatada}")
else:
    print(f"Em dia, última transação foi no dia: {data_formatada}")
#print(data_organizada)
#print(tempo_transacao.days)

'''
## Data e hora em diferentes fusos horários

Uma empresa tem escritórios em São Paulo, Nova York e Tóquio. Crie um script Python que mostra a data e hora atuais nesses três fusos horários. Exiba, também, se estes escritórios estão abertos ou fechados (9h às 17h).

'''

from datetime import datetime
from zoneinfo import ZoneInfo  


def esta_aberto(hora_local):
    if 9 <= hora_local.hour < 17:
        return "Aberto"
    else:
        return "Fechado"


sao_paulo = datetime.now(ZoneInfo("America/Sao_Paulo"))
nova_york = datetime.now(ZoneInfo("America/New_York"))
toquio = datetime.now(ZoneInfo("Asia/Tokyo"))

print("São Paulo:", sao_paulo.strftime("%d/%m/%Y %H:%M"), "-", esta_aberto(sao_paulo))
print("Nova York:", nova_york.strftime("%d/%m/%Y %H:%M"), "-", esta_aberto(nova_york))
print("Tóquio:", toquio.strftime("%d/%m/%Y %H:%M"), "-", esta_aberto(toquio))

