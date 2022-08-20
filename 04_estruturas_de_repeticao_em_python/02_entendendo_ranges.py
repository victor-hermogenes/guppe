"""

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

range(valor_de_parada)

# Forma 1:
for num in range(11):
    print(num + 1)


OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1.

# Forma 2:
range(valor de inicio, valor de parada)

for num in range (4, 11):
    print(num)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1.

# Forma 3:

range(valor_de_inicio, valor_de_parada, passo)

for num in range (5, 55, 5):
    print(num)

OBS: valor_de_parada não inclusive (início especificado pelo usuário e passo especificado pelo usuário)

# Forma 4 (Inversa):

range(valor_de_inicio, valor_de_parada, passo)

for num in range(10, -1, -1):
    print(num)

OBS: valor_de_parada não inclusive (início especificado pelo usuário e passo especificado pelo usuário)
"""



