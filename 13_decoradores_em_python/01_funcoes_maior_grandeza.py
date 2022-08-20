"""
Funções de Maior Graneza - Higher Order Functions - HOF

O que isso significa?

- Quando uma linnguagem de programação suporte HOF, indica que podemos ter funções
que retornem outras funções como resultado, ou mesmo, que podemos passar funções
como argumentos para outras funções, e até mesmo criar variáveis do tipo de funções
nos nossos programas.

OBS: Na seçã de funções, nós utilizamos isso.

Em Python, as funções são Cidadões de Primeira Classe, First Class Citizen

# Exemplo - Definindo as funções


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções

print(calcular(4, 3, somar))

print(calcular(4, 3, subtrair))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))

# Nested Functions - Funções Aninhadas


Em Python, podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
ou também Innver Functions (Funções Internas)

# Exemplo

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa

# Testando

print(cumprimento('Angelina'))

print(cumprimento('Felicity'))

# Retornando funções de outras funções

from random import choice


def faz_me_rir():
    def rir():
        return choice(('hahahahahahahaha', 'kkkkkkkkkkkkkk', 'yayayayayayayayayaya'))
    return rir


# Testando

rindo = faz_me_rir()
print(rindo())
"""

# Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo de funções mais externas.

from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahaha', 'lolololololo', 'kkkkkkkkkkkkkkk'))
        return f'{risada} {pessoa}'
    return dando_risada()


# Testando

print(faz_me_rir_novamente('Fernanda'))
print(faz_me_rir_novamente('Fernanda'))
print(faz_me_rir_novamente('Fernanda'))
