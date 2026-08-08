'''
Calculando a idade

Um usúario fornece sua data de nascimento no formato "dd/mm/aaaa". Crie um script Python que calcula a idade do usuário.

'''

from datetime import datetime,date
import locale
locale.setlocale(locale.LC_TIME,"pt_BR")

data_atual = date.today()

data_nascimento_usuario = input("Informe sua data de nascimento (dd/mm/aaaa): ")
data_formatada = datetime.strptime(data_nascimento_usuario,"%d/%m/%Y").date()

idade = (data_atual - data_formatada)//365

print(idade.days)
print(data_formatada)