"""
O bloco with

Passo para se trabalhar com arquivos
# 1 - Abrimnos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O block with é utilizado para criar um contexto de trabalho onde os recursos utilziados são fechados após o bloco with.

"""

# O block with

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
