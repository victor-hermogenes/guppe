"""
Módulo Collections - Named Tuple

# Recap tupla
tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> São tuplas diferenciadas, onde especificamos um nome e parâmetros para elas.
"""

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração namedtuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 = Declaração namedtuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 = Declaração namedtuuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)

# Acessando os dados

# Forma 1

print(ray[0])   # idade
print(ray[1])   # nome
print(ray[2])   # raca

# Forma 2

print(ray.idade)    # idade
print(ray.raca)    # raca
print(ray.nome)    # nome

print(ray.index('Chow-Chow'))

print(ray.count('Chow-Chow'))
