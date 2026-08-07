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
data_inicio = datetime(2026,9,9)
if data_hora_atual >=data_inicio:
    print("Projeto já começou!")
else:
    print("Projeto ainda não começou")