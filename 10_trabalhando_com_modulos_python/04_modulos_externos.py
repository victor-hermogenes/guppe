"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado pip - Python Installer Package

Você pode conyhecer todos os pacotes externos oficiais em : https://pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal.

Instalando um módulo:

pip install nome-do-modulo

# Instalando o pacote colorama

pip install colorama

# Utilizando o pacote instalado:

from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')
"""

import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1>')

with open('pydf_test_doc.pdf', 'wb') as f:
    f.write(pdf)

