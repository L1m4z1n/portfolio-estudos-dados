'''
Guia para a biblioteca 'datetime' em Python

A biblioteca 'datetime' em Python fornece objetos para manipulação de datas e horas. Aqui está um guia simples para algumas das funções mais úteis deste módulo.

datetime.datetime.now()

A função 'now()' retorna a data e a hora atuais.
'''
from datetime import datetime

data_hora_atual = datetime.now()

print(data_hora_atual)


'''
.date() -> pega a data apenas

.time() -> pega o horário apenas
'''
print(data_hora_atual.date())
print(data_hora_atual.time())

# Para pegar as informações de uma data é mais intuitivo

#ano = data_hora_atual.year()
#mes = data_hora_atual.month()
#dia = data_hora_atual.day()
#hora = data_hora_atual.hour()
#minutos = data_hora_atual.minute()
#segundos = data_hora_atual.second()

# datetime.date.today()

dia_hoje = datetime.date.today()
print(dia_hoje)

# datetime.timedelta()
# A classe 'timedelta' é usada para realizar operações com datas (adição e subtração)
from datetime import datetime, timedelta
data_inicio = datetime(2026,2,15)
duracao = 387
data_final = data_inicio + timedelta(days=duracao)
print(data_final)

#semana
duracao_semana = 15
data_final = data_inicio + timedelta(weeks=duracao_semana)
print(data_final)

# Calcular a diferença entre duas datas

tempo_projeto = data_final - data_inicio
print(tempo_projeto)
print(type(tempo_projeto))

nova_data_inicio = datetime(2026,4,15)
nova_data_fim = nova_data_inicio + tempo_projeto
print(nova_data_fim)


# Comparação entre datas

#passado < presente < futuro
data_hora_atual = datetime.now()
data_inicio = datetime(2026,1,1)
if data_hora_atual >=data_inicio:
    print("Projeto já começou!")
else:
    print("Projeto ainda não começou")
