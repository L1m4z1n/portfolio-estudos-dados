from datetime import datetime, timezone, timedelta
import locale
locale.setlocale(locale.LC_TIME,"pt_BR")

fuso_horario_sp = timezone(timedelta(hours=-3))
data_inicio = datetime(2026,2,15,15,25, tzinfo=fuso_horario_sp)