"""
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python

def soma(a, b):
    Soma os números a e b

    # >>> soma(1, 2)
    3

    # >>> soma(4, 6)
    10

    return a + b


print(soma(3, 4))


Para rodar um test do doctest:

python -m doctest -v nome_do_modulo.py

# Saída:

Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    03_doctests
1 items passed all tests:
   1 tests in 03_doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

# Outro exemplo

def duplicar(valores):

    # Duplica valores em uma lista

    # >>> duplicar([1, 2, 3, 4])
    # [2, 4, 6, 8]

    # >>> duplicar([])
    # []

    # >>> duplicar(['a', 'b', 'c'])
    # ['aa', 'bb', 'cc']

    # >>> duplicar([True, None])
    # Traceback (most recent call last):
        ...
    # TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    return [2 * elemento for elemento in valores]

# Saída:

Trying:
    duplicar([1, 2, 3, 4])
Expecting:
    [2, 4, 6, 8]
ok
Trying:
    duplicar([])
Expecting:
    []
ok
Trying:
    duplicar(['a', 'b', 'c'])
Expecting:
    ['aa', 'bb', 'cc']
ok
Trying:
    duplicar([True, None])
Expecting:
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
ok
1 items had no tests:
    03_doctests
1 items passed all tests:
   4 tests in 03_doctests.duplicar
4 tests in 2 items.
4 passed and 0 failed.
Test passed.

# Erro inesperado...

Obs.txt: Dentro do doctest, o Python não reconehce string com aspas duplas. Precisa ser aspas simples.

Certo:
def fala_oi():
    # Fala oi

    # >>> fala_oi()
    # 'oi'

    return "oi"

Errado:
def fala_oi():
    # Fala oi

    # >>> fala_oi()
    # "oi"

    return "oi"
"""

# Um último caso estranho...


def verdade():
    """Retorna verdade

    >>> verdade()
    True
    """
    return True
