"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Pythin, utilizamos a função integrada open()

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que neste caso, o nome do
arquivo a ser lido. Essa função retorna um -io.TextIOWrapper e é com ee trabalhamos então.

https://docs.python.org/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Ester aquivo deve existir u teremos o erro
FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='UTF-8'>

mode r -> Modo de Leitura. r -> read() -> ler

"""

# Exemplo

arquivo = open('texto.txt')

# print(arquivo)
# print(type(arquivo))

# para ler o conteúdo de um arquivo após sua abertura, devemos utilizar a função read()

ret = arquivo.read()
print(type(ret))
print(ret)
print(arquivo.read())

# OBS: O Python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor,
# funciona como o cursor que estamos escrevendo.

# OBS: A função read() lê todo o conteúdo do arquivo.

arquivo.close()
