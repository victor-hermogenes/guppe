"""
adicao = list([])
pergunta = input('Gostaria de adicionar algo a lista? ')


while pergunta != 'nao':
    confirmacao = str(input('O que mais? '))
    if confirmacao != 'nao':
        adicao.append(confirmacao)
        print(adicao)
    else:
        break
"""


"""
Listas (list)

Listas em Python funcionam como vetores/matrizes (arrays) em outras liguagens, com a diferença
de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se vocÇe criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

Listas são mutáveis: Ou seja, elas podem mudar constantemente.

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['V', 'i', 'c', 't', 'o', 'r', ' ', 'G', '.', 'H', 'e', 'r', 'm', 'g', 'e', 'n', 'e', 's']

lista3 = []

lista4 = list(range(11))

lista5 = list('Victor G. Hermogenes')

# Podemos facilmente checar se determinado valor está contido na lista.
num = int(input('Qual número vocês está procurando? '))
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordernar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas

Para adicionar elementos em listas, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# OBS: Com append, nós só conseguimos dicionar 1 elemento por vez
# lista1.append(12, 34, 56) # Erro

lista1.append([8, 3, 1]) # Inclui na lista como elemento único (adiciona a lista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 24, 67]) # Inclui cada elemento da lista como valor adicional à lista (extende a lista)
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.

lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos facilmente juntar duas listas

# lista6 = lista1 + lista2
# lista1.extend(lista2)
# lista1 = lista1 + lista2

# É possível imprimir a lista em reverso

# Forma 1
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos temos dentro da lista
print(len(lista5))

# Podemos remover facilmente o último elemento de uma lista
# OBS: O pop não somente remove o último elemento, mas também o retorna
print(lista5)
lista5.pop()
print(lista5)


# Podemos remover um elemento pelo índice
# OBS: Os elementos à direita deste índice, foram deslocados para a esquerda
# OBS: Se não houver elemento no índice informado, teremos o erro IndexError

lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

Abaixo estamos colocando um delimitador de espaço através do comando join (que permite a liberdade de escolher qual
o delimitador), transformando a lista em string
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2.35, True, 'Victor', 'V', [1, 2, 3], 4345315144]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 - Utilizando for

soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando While
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou difite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']

#           0          1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])    # verde
print(cores[1])    # amarelo
print(cores[2])    # azul
print(cores[3])    # branco

# Fazer acesso aos elementos de forma indexada inversa
print(cores[-4])    # verde
print(cores[-3])    # amarelo
print(cores[-2])    # azul
print(cores[-1])    # branco

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
    
# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

# Outros métodos não tão importantes mas também úteis

# Encontrar o índice de um elemento na lista
numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice está o valor 6?
print(numeros.index(6))

# Em qual índice está o valor 9
print(numeros.index(9))

# Em caso de duplicidade do valor, ele retorna o indice do primeiro valor encontrado
print(numeros.index(5))

# Podemos fazer busca em um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1)) #Buscando a partir do indice 1

# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError

# Revisão de slicing

# lista(inicio:fim:passo)
# range(inicio:fim:passo)

# Trabalhando com slice de lista com o parâmentro 'início'
lista = [1, 2, 3, 4]

print(lista[1:])    # Iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parâmentro 'fim'

print(lista[:2])    # Começa em 0 e vai até o índice escolhido - 1

# Trabalhando com slice de passo em passo

print(lista[1::2])

# Invertendo valores em uma lista
nomes = ['Victor', 'G.', 'Hermogenes']

nomes[0], nomes[1], nomes[2] = nomes[2], nomes[1], nomes[0]
print(nomes)

nomes = ['Victor', 'G.', 'Hermogenes']
nomes.reverse()
print(nomes)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho de uma lista

# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))   # soma
print(max(lista))   # máximo valor
print(min(lista))   # mínimo valor
print(len(lista))   # tamanho da lista

# Trabsformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos mais elementos para desempacotador do que variáveis para receber, teremos um ValueError
# O contrário também se aplica.

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()    # cópia
print(nova)

nova.append(4)
print(nova)

# Veha que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python
# É chamnado de Deep Copy.

# Forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista    # Atribuição
print(nova)

nova.append(4)
print(nova)
print(lista)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# Após realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy.

"""




