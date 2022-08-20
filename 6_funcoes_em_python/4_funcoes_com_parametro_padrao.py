"""
Funções com Parâmetro Padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função com passagem de parâmetro opcional:
print('Victor Gonzalez')
print()

# Exenoki de função com passagem obrigatória:
def quadrado(numero):
    return numero ** 2


print(quadrado(3))
print(quadrado())   # TypeError

# Certo

def exponencial(numero=4, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))    # 2 * 2 * 2 = 8
print(exponencial(3, 2))    # 3 * 3 = 9

print(exponencial(3))   # Por padrão eleve ao quadrado
print(exponencial(3, 5))    # Eleca a potência informada pelo usuário

# OBS:
# Se o usuário passar somente 1 parâmetro, será atribuído ao parâmetro número, e será calculado o quadrado dele;
# Se o usuário passsar 2 argumentos, o primeiro será atribuído ao parâmetro número e o segundo ao potência, Então
# será calculada esta potência.

print(exponencial())

# OBS: Em funções Pythons, os parãmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

# Erro


def teste(num=2, potencia):
    return num ** potencia


# Certo


def teste(potencia, num=2):
    return num ** potencia

# Outros exemplos

# Errado


def soma(num1, num2):
    return num1 + num2


print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())   #Type Error

# Certo


def soma(num1=4, num2=3):
    return num1 + num2


print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())   #Type Error

# Exemplo mais complexo


def mostra_informacao(nome='Victor', aluno=False):
    if nome == 'Victor' and aluno:
        return f'Bem-vindo aluno {nome}'
    elif nome == 'Victor':
        return 'Eu pensei que você era o aluno'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(aluno=True))
print(mostra_informacao('Ozzy'))

Por quê utilizar parâmetros com valor default?

- Nos permite ser mais flexíveis com funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com mais exemplos legíveus de código.

Quas tipos de dados podemos utilizar como valores defaut para parâmetros?
- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funçõies e etc.

# Exemplos de funções como parâmetros


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao (num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Victor'    # Variável global


def diz_oi():
    instrutor = 'James'    # Variável local
    return f'Oi {instrutor}'


print(diz_oi())

# Se existir uma variável local dentro da função, ela substituirá a variável global

def diz_oi():
    prof = 'Victor'
    return f'Olá {prof}'


print(diz_oi())

print(prof)    # NameError

# Variáveis locais não existem fora das funções.

# Errado

total = 0


def incrementa():
    total = total +1
    return total


print(incrementa())    # UnboundLocalError

# A variável local não conseguirá usar a variável global como definição para processar a função

# ATENÇÃO com variáveis globais (Se puder evitar, evite!)

# Certo

total = 0


def incrementa():
    global total
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())

# Usando a função global, é possível dizer a definição que estaremos usando a variável global na sua construção
# sem precisar definir uma variável local

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável


def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador +1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())

# OBS: A função dentro() só é conhecida dentro da definição da função fora(), a tentativa de usar ela acarretará em erro
"""

