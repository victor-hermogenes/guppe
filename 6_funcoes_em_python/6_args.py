"""
Entrnendo o *args
- O *args é um parâmetro, como outro qualquer. Isso significa que poderá chamar
de qualquer coisa, desde que comece com asterisco.

Exemplo:

Mas pro convenção, utilizamnos *args para definí-lo

Mas o que é o *args

O parâmetro *args é utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então lembre-se que tuplas são umitáveis.

# Entendo o args


def soma_todos_numeros(nome, email, *args):
    return sum(args)


print(soma_todos_numeros('Angelona', 'Jolie'))
print(soma_todos_numeros('Angelona', 'Jolie', 1))
print(soma_todos_numeros('Angelona', 'Jolie', 2, 3))
print(soma_todos_numeros('Angelona', 'Jolie', 2, 3, 4))
print(soma_todos_numeros('Angelona', 'Jolie', 3, 4, 5, 6))

# Outo exemplo da utilização do *args


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza quem você é ...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))
print(verifica_info(1, 'Geek', 3.145, 'University'))

"""


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador

print(soma_todos_numeros(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados.
# Desta forma ele saber que deverá antes desempactoar estes dados.