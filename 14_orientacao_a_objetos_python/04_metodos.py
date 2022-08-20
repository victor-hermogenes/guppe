"""
POO - Métodos

- Métodos -> Representam o comportamento do objeto. Ou seja, as alões
que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos em 2 grupos: Métodos de Instância e
Métodos de Classe

# Métodos de Instância

# O método __init__ é um método especial chamado de construtor e
sua função é construir o objeto a partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

OBS: Os métodos/funções dunder em Python são chamados de métoidos mágicos

ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando dunder, não é aconselhado.
Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento
dessas funções. Então, evite ao máximo, de preferência nunca o faça.

p1 = Produto('Playstation 4', 'Video Game', 2300)

print(p1.desconto(50))

print(Produto.desconto(p1, 40))    # self, desconto

user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')

print(user1.nome_completo())
print(user2.nome_completo())

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(42)

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user._Usuario__senha}')

# Métodos de Classe em Python são conhecidos como Métodos Estáticos em outras linguagens

# Métodos de classe

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

Usuario.conta_usuarios()    # Forma correta
user.conta_usuarios()    # Possível, mas incorreta

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

print(user._Usuario__gera_usuario())    # Acesso, de forma ruim...
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self._ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return(self.__valor * (100 - porcentagem)) / 100

from passlib.hash import  pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


# Método estático

print(Usuario.contador)

print(Usuario.definicao())

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

print(user.contador)

print(user.definicao())
