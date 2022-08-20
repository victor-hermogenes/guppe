"""
Geradores

- Geradores ( Generators) são Iterators (Iteradores);

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator

Outras informações:
- Generators podem ser cirados com funções geradores;
- Funções geradores utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)

------------------------------------------------------------------------------------------------
| Funções                                             | Generator Functions                    |
------------------------------------------------------------------------------------------------
| utilizam return                                     | utilizam yield                         |
------------------------------------------------------------------------------------------------
| retorna uma vez                                     | podem utilizar yield múltiplas vezes   |
------------------------------------------------------------------------------------------------
| quando executada, retorna um valor                  | quando executada, retorna um generator |
------------------------------------------------------------------------------------------------

gen = conta_ate(5)

# print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for num in gen:
    print(num)

print(next(gen))    # 1

print('Geek')

for n in gen:
    print(n)
"""

# Exemplo de Função Geradora - Generator Function


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# OBS: Uma Generator Function não é um Generator, ele gera um generator.


gen = list(conta_ate(10))

print(gen)
