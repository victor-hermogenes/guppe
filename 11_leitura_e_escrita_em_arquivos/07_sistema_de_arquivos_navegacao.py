"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos improtar
e fazer uso do módulo OS.

OS -> Operating System - Sistema Operacional

# getcwd() -> pega o current work directory - diretório de trabalho atual
# Retorna o path (caminho) absoluto
print(os.getcwd())    # /home/victorgh/PycharmProjects/guppe/11: Leitura e Escrita em Arquivos

# Para mudar o direitório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())    # /home/victorgh/PycharmProjects/guppe

os.chdir('..')

print(os.getcwd())    # /home/victorgh/PycharmProjects

os.chdir('..')

print(os.getcwd())    # /home/victorgh

os.chdir('..')

print(os.getcwd())    # /home

os.chdir('..')

print(os.getcwd())    # /

# odemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('/home/victorgh'))    # True

# OBS para usuários Windows
# Se você infelizmente estiver utilizando um computador com Windows,
# terá que ter cuidado ao verificar diretorios.
# Use o '\' duas vezes em Windows

print(os.path.isabs('C:\\Users\\victorgh'))

# Podemos identificar o sistema operacional com o módulo os
print(os.name)    # posix (Linux, Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional
print(os.uname())

import sys

print(sys.platform)

# '/home/victorgh/workspace/sistema

print(os.getcwd())    # /home/victorgh/PycharmProjects/guppe/11: Leitura e Escrita em Arquivos

res = os.path.join(os.getcwd(), '..', 'geek', 'university')

os.chdir(res)

print(os.getcwd())    # /home/victorgh/PycharmProjects/guppe/geek/university

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o
# diretório que será juntado ao atual.

# Podemos listar os arquivos e diretório com o listdir()
print(arquivos[0].name)
print(os.listdir('/etc'))
"""

# Fazer o import
import os

# Podemos listar os arquivos e diretórios com mais detalhes com o scandir()

scanner = os.scandir()

arquivos = list(scanner)

# print(arquivos)

# print(dir(arquivos[0]))

print(arquivos[0].inode())    # ??
print(arquivos[0].is_dir())    # É um diretório? False
print(arquivos[0].is_file())    # É um arquivo? True
print(arquivos[0].is_symlink())    # É um link simbólico? False
print(arquivos[0].name)    # Nome do arquivo
print(arquivos[0].path)    # Caminho até o arquivo
print(arquivos[0].stat())    # Estastísticas

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la assim quando abrimos um arquivo.

scanner.close()