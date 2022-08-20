"""
Sistema de Arquivos - Manipulação

# Descobrindo se um arquivo ou diretório existe
print(os.path.exists('arquivo.txt'))    # False
print(os.path.exists('frutas.txt'))    # True

# Diretório

# Paths relativos
print(os.path.exists('../geek'))    # True
print(os.path.exists('../geek/university'))
print(os.path.exists('../geek/university/geek3.py'))    # True
print(os.path.exists('../geek/outro'))    # False


# Paths absolutos
print(os.path.exists('/home/victorgh/university'))    # False
print(os.path.exists('/home/victorgh/Imagens'))    # True
print(os.path.exists('/home/victorgh/Imagens/'))    # True

# Criando arquivos

# Forma 1
open('arquivo.teste.txt', 'w').close()

# Forma 2
open('arquivo.teste2.txt', 'w').close()

# Forma 3
with open('arquivo.teste3.txt', 'w') as arquivo:
    pass

# Forma 4
os.mknod('arquivo-teste4.txt')

os.mknod('/home/victorgh/university.txt')

# OBS: Se você estiver utilizando no Mac OS, pode have um erro de PermissionError

# OBS: Criando um arquivo via mknod(), se o arquivo já existir teremos o erro FileExistsError

# Criando Diretórios - úncios (um a um)
# Path Relativo
os.mkdir('templates')

# OBS: A função mkdir() cria um diretório, caso ele já exista teremos FileExistsError

# Path Absoluto
os.mkdir('/home/victorgh/templates')

os.mkdir('/etc/templates')

# OBS: Se não tivermos permissão para criar o diretório, teremos um PermissionError

# Criando multi-diretórios (árvore de diretórios)
os.makedirs('templates/geek/university/outro')

# OBS: Se já existir, teremos um FileExistsError

os.makedirs('templates2/novo2/outro2', exist_ok=True)

# Renomear arquivo e diretorios

os.rename('geek2/novo2', 'geek2')

# OBS: Se o diretório não existir teremos um FileNotFoundError

# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Renomear arquivo e diretorios

# Arquivos
os.rename('geek2/novo2/outro2/teste.txt', 'geek2/novo2/outro2/geek.txt')

# OBS: Se quisermos renomear um arquivo dentro de um diretório, é preciso passar todo o caminho no novo nome até chegar
# no que vai ser renomeado.

# ATENÇÃO! Tome cuidado com os camndo de deleção. Ao deletarmos um arquivo ou diretório, eles
# não vão para a lixeira, eles somem

os.remove('geek.txt')

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.

# Caso o arquivo não exista depois da deleção, teremos o erro FileNotFoundError

# OBS: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError

# Removendo diretórios vazios

os.rmdir('templates')

# OBS: Se o diretório tiver qualquer conteúdo, teremos um OSError

# OBS: Se o diretório não existir, teremos um FileNotFoundError

# Removendo uma árvore de arquivos

for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Podemos remover uma árvore de direórios vazios
os.removedirs('geek2/mais/mais')

# Se algum dos diretório contiver arquivos e outros diretório, o processo para.

# ATENÇÃO: Ao remover arquivos e diretórios com Python, eles não vão para a lixeira, eles vão embora

# Importando a biblioteca send2trash (Envia arquivos e diretórios para a lixeria)

from send2trash import send2trash

os.remove('cesta1.txt')    # Não vai para a lixeira. É deletaddo imediatamente

send2trash('cesta2.txt')    # Vai para lixeira, pode ser restaurado

# OBS: Se o arquivo não existir, teremos OSError

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquvio_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University \n')
    input()

# Estamos criando um diretório temporário, abrindo ele e criando um arquvi para escrevermos um texto.
# No final, usamos um input() só para mantermos os arquivos temporários 'vivos' dentro dos blocos with

# OBS: possivelmente o código acima não irá funcionar se você estiver utilizando Windows, por conta dele trabalhar
# de fomra difernete com arquivos temporários.

# Criando um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# Em arquivos temporário só conseguimos escrever bit. Por isso utlizamos b''

https://docs.python.org/3/library/os.html?highlight=os#module-os
"""

import os
import tempfile

