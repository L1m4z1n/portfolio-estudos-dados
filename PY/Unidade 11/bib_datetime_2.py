'''
Guia para a biblioteca 'datetime' em python

A biblioteca dateitme em pyhton fornece objetos para manipulação de datas e horas. Aqui está um guia simples para algumas das funções mais úteis deste módulo.

datetime.datetime.strftime()

A função strftime() converte um objeto datetime para um string de acordo com um formato específico.
Símbolos qu podem ser usados para formatar datas podem ser achados aqui(era um link do curso kkkkkk)

'''

from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME,"pt_BR")

data_inicio = datetime(2026,2,15)

data_inicio_texto = data_inicio.strftime("%d de %B de %Y, %A")
print(data_inicio_texto)


'''
datetime.datetime.strptime()

Analisa uma string representando uma data e hora de acordo com um formato. O retorno é um objeto datetime
'''
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME,"pt_BR")
data_inicio_texto = "15 de fevereiro de 2026 às 15:25"
data_inicio = datetime.strptime(data_inicio_texto,"%d de %B de %Y às %H:%M")
print(data_inicio)


'''
Trabalhando com fuso horário

Podemos criar um objeto datetime. O construtor da classe aceita os seguintes argumentos:

-year: ano
-month: mês
-day: dia
-hour: hora
-minute: minuto
-second: segundo
-microsecond: microssegundo
-tzinfo:fuso horário
'''

'''
Os horários que vimos até o momento são os que chamamos de ingênuos (naive). Eles não possuem informações sobre o fuso horário. Para criar um horário consciente (aware), precisamos passar um objeto tzinfo para o construtor da classe datetime. O módulo datetime fornece uma classe timezone que pode ser usada para criar um objeto tzinfo. No exemplo abaixo, usamos UTC como fuso horário. UTC significa Tempo Universal Coordenado, que é o fuso horário de referência a partir do qual todos os outros fusos horários são calculados.
UTC
'''
from datetime import datetime, timezone, timedelta
import locale
locale.setlocale(locale.LC_TIME,"pt_BR")

fuso_horario_sp = timezone(timedelta(hours=-3))
data_inicio = datetime(2026,2,15,15,25, tzinfo=fuso_horario_sp)
