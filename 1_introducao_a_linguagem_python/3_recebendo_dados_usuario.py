"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas simples -> 'Victor'
- Aspas duplas -> "Victor"
- Aspas simples triplas -> '''Victor'''
"""
# - Aspas duplas triplas -> """Victor"""

# Entrada de dados
# Jeito 1:
# print("Qual seu nome?")
# nome = input() # Input -> Entrada

# Jeito 2:
nome = input('Qual seu nome? ')

# Exemplo de print 'antigo' 2.x
# print('seja bem-vindo(a) %s' % nome_

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

# Jeito 1:
# print("Qual sua idade?")
# idade = input()

# Jeito 2:
idade = input('Qual a sua idade? ')

# Processamento

# Saída de dados

# Exemplo de print 'antigo' 2x
# print('O %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('O(A) {0} tem {1} anos'.format(nome, idade))

# Exemplo 'mais atual' 3.7
print(f'O(A) {nome} tem {idade} anos')

"""
# int(idade) => cast

cast é a 'conversão' de um tipo e dado para outro
"""
print(f'O(A) {nome} nasceu em {2022 - int(idade)}')