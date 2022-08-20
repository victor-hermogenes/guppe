"""
Filter

filter () -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)
print(f'Média: {media}')

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável

res = filter(lambda x: x < media, dados)
print(list(res))

# OBS: Assim como na função map (), após serem utilizados os dados de filter(), eles são excluídos da memória
print(f'Novamente: {list(res)}')

# Forma simples

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)
print(list(res))

# Forma lambda

# 1

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(lambda x: x != '', paises)
print(list(res))

# 2

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

# A diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento
# do iterável.

# filter () -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de
# acordo com a função

# Exemplo mais complexo

usuarios = [
    {"usarname": "samuel", "tweets": ["Eu adoro bolosm", "Eu adoro pizzas"]},
    {"usarname": "carla", "tweets": ["Eu amo meu gato"]},
    {"usarname": "jeff", "tweets": []},
    {"usarname": "bob123", "tweets": []},
    {"usarname": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"usarname": "gal", "tweets": []},

]

print(usuarios)

# Filtrar os usuários que estão inativos no Twitter

# Forma 1:
# inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda u: not u['tweets'], usuarios))
print(inativos)


"""

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda instrutora: len(instrutora) < 5, nomes)))

print(lista)

