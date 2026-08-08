
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

