"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade
de ocorrências desse elemento.

# Realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma Lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 5, 3: 5, 2: 4, 4: 3, 5: 2, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que, para cada elemento da lista o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Victor G. Hermogenes'))
# Counter({'e': 3, 'o': 2, 'r': 2, ' ': 2, 'V': 1, 'i': 1, 'c': 1, 't': 1, 'G': 1, '.': 1, 'H': 1, 'm': 1, 'g': 1, 'n': 1, 's': 1})

"""

from collections import Counter

# Exemplo 3

texto = """A Apollo 16 foi um voo espacial tripulado norte-americano responsável pelo quinto e penúltimo pouso na Lua. 
A missão foi a segunda planejada para realizar uma estadia mais longa na superfície lunar, ser focada em ciência e 
utilizar o Veículo Explorador Lunar para locomoção. A Apollo 16 foi lançada do Centro Espacial John F. Kennedy em 
Cabo Kennedy na Flórida por um foguete Saturno V no dia 16 de abril de 1972, porém ela sofreu de vários pequenos 
problemas no caminho para a Lua, culminando em um problema no propulsor do módulo de comando e serviço Casper que quase 
levou ao aborto da alunissagem.

Os astronautas John Young e Charles Duke alunissaram o módulo lunar Orion no dia 21 de abril nas Terras Altas de 
Descartes e passaram um total de 71 horas na superfície, vinte horas das quais em atividades extraveiculares. Os dois 
exploraram a região com o Veículo Explorador Lunar, semelhante ao que havia sido feito na Apollo 15, o que lhes 
permitiu atravessar mais de 26 quilômetros e coletar 95 quilogramas de material para análise na Terra. A região de 
Descartes fora escolhida para que os astronautas pudessem colher amostras geológicas bem mais antigas do que aquelas 
adquiridas em missões anteriores.

Ao mesmo tempo, o astronauta Ken Mattingly permaneceu em órbita lunar operando o Casper. Ele coletou vários dados sobre 
a Lua através dos instrumentos científicos do módulo e tirou centenas de fotografias da superfície. O Orion reencontrou 
depois com o Casper em órbita no dia 24 de abril a fim de retornarem para a Terra, mas antes lançaram uma pequeno 
subsatélite em órbita. Mattingly realizou uma caminhada espacial durante a viagem de volta para poder recuperar 
cartuchos de dados do módulo de serviço. Os três astronautas retornaram em segurança, com a missão tendo realizado 
todos os seus objetivos."""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))
