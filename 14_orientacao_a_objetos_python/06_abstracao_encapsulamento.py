"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando
classes.

Encapsular -> cápsula



             classe
---------------------------------
/                               /
/     Atributos e métodos       /
/_______________________________/

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo
um atributo privado chamado __nome e um método provado
chamado __falar()

Esses elementos privados só devem/deveriam ser acessados
dentro da classe. Mas Python não bloqueia este acesso
fora da classe. COm Python acontece um fenômeno chamado
name Mangling, que faz uma alteração na forma de se
acessar os elementos privados, confor:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome
instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dads relevantes de uma classe, escondendo atributos e métodos
provados do usuário.

print(conta1.__dict__)

conta1.depositar(150)

print(conta1.__dict__)

conta1.sacar(200)

print(conta1.__dict__)
"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor precisa ser positivo')

    def transferir(self, valor, conta_destino):
        # 1 - Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10 # Taxa de transferência para quem enviou

        # 2 - Adicionar o valor na conta do destino
        conta_destino.__saldo += valor


# Testando

conta1 = Conta('Geek', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Felicity', 300, 2000)
conta2.extrato()

conta2.transferir(100, conta1)
conta1.extrato()
conta2.extrato()
