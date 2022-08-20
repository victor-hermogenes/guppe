"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

C ou Java

for(int i = 0; i < limitador; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis
 - String
    nome = 'Victor'
 - Lista
    lista = [1, 3, 5, 7, 9]
 - Range
    numeros = range(1, 10)

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)


# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)


# Exemplo de for 3 (Iterando sobre um range)

range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.

for numero in range(1, 10):
    print(numero)


enumerate: # Enumera o nome
((0, 'V')(1, 'i')(2, 'c')(3, 't')(4, 'o')(5, 'r')(6, ' ')(7, 'G')(8, '.')(9, ' ')(10, 'H')(11, 'e')(12, 'r')(13, 'm')(14, 'o')(15, 'g')(16, 'e')(17, 'n')(18, 'e')(19, 's'))


for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

for letra in nome:
    print(letra, end='')

Tabela de Emojis unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""

# Original U+1F618
# Modificiado 	U0001F618

beijos = int(input(f'Quantos beijos vai enviar? '))
qtd = 0

for n in range(1, beijos + 1):
    beijinhos = int(input(f'{n}/{beijos} beijos, envia mais porra! '))
    qtd = qtd + beijinhos
    print(f'{qtd} beijinhos \U0001F618 \nParanbéns, isso é muito gay')