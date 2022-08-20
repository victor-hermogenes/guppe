"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais;
     - Variáveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa.

2 - Varíaveis locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.


Para declarar variáveis em Python fazemos:

nome_da_variável = valor_da_variável

Python é uma linguagem de tipagem dinâmica, Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor a ela.

Exemplo em C:
int numero = 42;

Exemplo em Java
int numero = 42;
"""

numero = 4    # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existo = '01'
print(nao_existo)

numero = 2

if numero > 10:
    novo = numero + 10    # A variável 'novo' está declarada localmente dentro do bloco do if. Portanto, é local
    print(novo)

print(novo)
