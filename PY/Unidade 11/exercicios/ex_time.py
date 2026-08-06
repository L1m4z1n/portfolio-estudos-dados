import time
import locale
'''
## Contagem regressiva

Um evento especial está programado para começar em 10 segundos. Crie uma contagem regressiva que começa em 10 e vai até 0, com uma pausa de um segundo entre cada número.

'''

#for i in range(10):
#    time.sleep(1)
#    print(f"Faltam {10 - i} segundos para começar")

'''
## Formatação de tempo

Uma empresa quer exibir a data e a hora atual em seu site no formato "Dia da semana, dia de mês de ano, horas:minutos". Crie um script Python que mostra a data e a hora atuais neste formato.

'''

#locale.setlocale(locale.LC_TIME,"pt_BR")
#data_atual = time.localtime()
#data_texto = time.strftime("%A, %d de %B de %Y, %H:%M", data_atual)

#print(data_texto.title())

'''
## Tempo de execução

Quanto tempo o código abaixo vai demorar para executar? Vamos gerar um número para cada um dos funcionários de uma empresa e colocar em uma lista para sortear o funcionário vencedor de um prêmio especial de uma viagem de fim de ano. Quanto tempo seu código demora para criar essa lista de números a serem sorteados?
'''

#tempo_inicial = time.time()

#sorteio_funcionarios = []
#qtde_funcionarios = 100000000
#for i in range(qtde_funcionarios):
#    num_funcionarios = i
#    sorteio_funcionarios.append(i)

#tempo_final = time.time()
#print(f"Demorou {tempo_final} segundos para rodar o código")


'''
## Bases de dados mal formatadas

Bases de dados formatadas de forma incorreta é uma das coisas mais comuns em projetos de análise de dados. Sua tarefa é conseguir extrair a data no formato correto de 2 listas de datas diferentes, para podermos futuramente analisar essas datas.
'''
lista_datas1 = [
    "15 de julho de 2026",
    "22 de agosto de 2026",
    "10 de outubro de 2026",
    "30 de dezembro de 2026",
    "14 de janeiro de 2027",
    "05 de março de 2027",
    "19 de maio de 2027",
    "07 de setembro de 2027",
    "12 de novembro de 2027",
    "25 de dezembro de 2027",
    "02 de fevereiro de 2028",
    "18 de abril de 2028",
    "31 de julho de 2028",
    "11 de outubro de 2028",
    "20 de dezembro de 2028"
]
lista_datas2 = [
    "07-14-2026",
    "09-05-2026",
    "11-20-2026",
    "01-12-2027",
    "03-28-2027",
    "06-15-2027",
    "08-02-2027",
    "10-31-2027",
    "02-14-2028",
    "05-22-2028",
    "09-09-2028",
    "12-25-2028",
    "04-01-2029",
    "07-19-2029",
    "11-11-2029"
]

lista_datas_formatadas = []
for data in lista_datas1:
    data_formatada = time.strptime(data,"%d de %B de %Y")
    lista_datas_formatadas.append(data_formatada)
for data in lista_datas2:
    data_formatada = time.strptime(data,"%m-%d-%Y")
    lista_datas_formatadas.append(data_formatada)
