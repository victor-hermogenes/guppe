"""
JSON e Pickle

JSON - JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas
(Twitter, Facebook, Youtube...) e terceiros (nós desenvolvedores).

import json

ret = json.dumps(['produto', {'PlaysStation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))

print(ret)

import json


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


shiro = Gato('Shiro', 'Branca')

print(shiro.__dict__)

ret = json.dumps(shiro.__dict__)

print(ret)

Integrando o JSON com o Pickle

pip install jsonpickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


shiro = Gato('Shiro', 'Branca')

ret = jsonpickle.encode(shiro)

print(ret)

# Escrevendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


shiro = Gato('Shiro', 'Branca')

with open('shiro.json', 'w') as arquivo:
    ret = jsonpickle.encode(shiro)
    arquivo.write(ret)

# Escrevendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


shiro = Gato('Shiro', 'Branca')

with open('shiro.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
"""

# Escrevendo o arquivo json/pickle

import jsonpickle


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


shiro = Gato('Shiro', 'Branca')

with open('shiro.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
