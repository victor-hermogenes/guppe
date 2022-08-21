"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yy 12:55:34.9939329
data_final = dd/mm/mm 13:34:23.0948484

delta = data_final - data_inicial
"""

import datetime

# Temos a data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
aniversario = datetime.datetime(2023, 7, 1, 0)

tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))

print(repr(tempo_para_evento))

print(tempo_para_evento)
