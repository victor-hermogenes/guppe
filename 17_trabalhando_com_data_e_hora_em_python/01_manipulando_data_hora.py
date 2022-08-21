"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime

import datetime

# print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

# Retorna a data e a hora corrente
print(datetime.datetime.now())    # 2022-08-21 17:58:19.004894

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

# replace para fazer ajuste na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o trabalho para 16 horas, 0 minuots, 0 segundos, 0 microsegundos
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)

# Recebendo dados do usuário e convertendo para data:

print(type(evento))

print(type('31/12/2018'))

print(evento)

nascimento = input('Informe sua data de nascimento (dd/mm/yy): ')

print(nascimento)

print(type(nascimento))

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(type(nascimento))
"""

import datetime

evento = datetime.datetime.now()

# Acesso individual dos elementos de data e hora

print(evento.year)    # ano
print(evento.month)    # mês
print(evento.day)    # dia
print(evento.hour)    # hora
print(evento.minute)    # minuto
print(evento.second)    # segundo
print(evento.microsecond)    # microsegundo

print(dir(evento))



