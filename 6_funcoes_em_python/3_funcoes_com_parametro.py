"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados.;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se pensarmos numa função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada, mas não saída;
- Não possuem entrada, mas tem saída;
- Possuem entrada e saída;

# Refatorando uma função


def quadrado(numero):
    # return numero * numero
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

# Refatorando função


def cantar_parabens(aniversariante):
    for n in range(5):
        print('Parabéns pra você')
        print('Nessa data querida')
        print('Muitas felicidades')
        print('Muitos anos de vida')
        print(f'Viva o {aniversariante}!')


cantar_parabens('Victor')

# Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.

# Exemplo


def soma(a, b):
    return a + b


def multipica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(multipica(4, 5))
print(multipica(2, 8))

print(outra(3, 2, 'Victor '))
print(outra(5, 4, 'Python '))

# OBS: Se informamos um número errado de parâmentro ou argumentos, teremos TypeError

# Errado:
# print(soma(2, 5, 4))     TypeError - Passando argumentos a mais
# print(soma(4))     TypeError - Faltando um argumento

# Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Victor', 'Gonzalez'))

# A diferença entre Parâmetros e Argmentos:

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execuação de uma função;

# A ordem dos parâmetros importa!

nome = 'Felicity'
sobrenome = 'Jones'

print(sobrenome, nome)

# Argumentos nomeados (Keyword Argumens)

# Caso utilizamos nomes dos parâmetros nos argumentos para informálos, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Gonzalez', nome='Victor'))

# Erro comum na utilização do return

# Errado

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
        return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

# Certo

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))
"""
numeros = 0
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

