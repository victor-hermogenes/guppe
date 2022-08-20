"""
Tipo string

Em Python um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Victor G. Hermogenes'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings

print(nome[0:6])    # Slice de string

print(nome[7:20])   # Slice de String

# [    1,     2,         3]
# ['Victor', 'G.', 'Hermogenes']
print(nome.split()[0])

print(nome.split()[1])
"""
# Estiver entre àspas duples triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14,  15,  16,  17]
# ['V', 'i', 'c', 't', 'o', 'r', 'G', '.', 'H', 'e', 'r', 'm', 'o', 'g', 'e', 'n', 'e', 's']
nome = 'Victor G. Hermogenes'

"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta.
"""
print(nome[::-1])   # Inversão da Sting Pythônico

print(nome.replace('e', 'P'))

print(nome.lower().replace('e', 'Pica mlk')[::-1])

texto = 'socorram me subino onibus em marrocos'     # Palíndromo
print(texto)
print(texto[::-1])
