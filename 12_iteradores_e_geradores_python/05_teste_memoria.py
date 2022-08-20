"""
Teste de Memória com Generators

# Sequência de Fibonacci

1, 1, 2, 3, 4, 5, 8, 13...

# Função usando listas - 453M,1MB

def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Teste 1 453,1MB
for n in fib_lista(100000):
    print(n)

# Função usando geradores - 6,9MB


def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste 2 6,9MB
for n in fib_gen(100000):
    print(n)

"""

# Função usando listas - 453M,1MB

def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Função usando geradores - 6,9MB


def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste 2 6,9MB
for n in fib_gen(100000):
    print(n)
