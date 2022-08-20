"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem duas diferenças básicas;

1 - As tuplas são repesentadas (não necessariamente criadas) por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla, ela não muda. Toda
operação em uma tupla, gera uma nova tupla.

# CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4)    # Isso não é uma tupla!
print(tupla3)
print(type(tupla3))

tupla4 = (4,)  # Isso é uma tupla!
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela "," e não pelo uso do "()".

(4) -> Não é tupla
(4,) -> É tupla
4, -> É tupla

# Podemos gerar uma tupla dinâmicamente com range (início, fim passo).
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Victor G. Hermogenes', 'Aprendendo a programar')

aluno, curso = tupla
print(aluno)
print(curso)

# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotar.

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho

# * Se os valores forem inteiros ou reais

tupla = (1, 2, 3, 4, 5)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas:

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

tupla1 = tupla1 + tupla2    # Tupla são imutáveis, mas podemos sobrescrever seus valores.
print(tupla1)

# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)

print(3 in tupla)
print(33 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('c'))

aluno = tuple('Victor G. Hermogenes')
print(aluno)

print(aluno.count('e'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1:
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# O acesso a elementos de uma tupla é semelhante a de uma lista

print(meses[5])

# Iterar com while

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificando em qual indice um elemento está na tupla
print(meses.index('Junho'))

# OBS: Caso o elemento não exista, será gerado erro

# Slicing

# tupla[início:fim:passo]

print(meses[5:9])

# Por que utiliar tuplas?

# - Tuplas são mais rápidas do que listas;
# - Tuplas deixam seu código mais seguro*;
# * Isso porque trabalhar com elementos imutáveis traz segurança aos códigios.

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla # Na tupla não temos o problema de Shallow Copy

print(nova)
print(tupla)

outra = (4, 5, 6)
print(outra)

nova = nova + outra

print(nova)
print(tupla)

"""
