"""
Por que testar o nosso código?

Testes Automatizados!


        Aplicação web
--------------------------------
/                              /
/     frontend e backend       /
--------------------------------
/    testes automatizados      /
--------------------------------

Por que testar nosso código?
    - Reduzir Bugs;
    - Testes garantem que novos recursos da aplicação não quebrem (alterem) recursos antigos;
    - Testes garantem que bugs (problemas) que foram corrigidos anteriormente, continuem assim;
    - Testes garantem que a refatoração que costuamos a fazer não tragam novos bugs (problemas);

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Com o TDD é utilizado estágios de desenvolvimento:
    - Você escreve o seu teste primeiro;
    - Então você escreve o códiugo mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso);
    - Então refatoria o código para realizar a funcionalidade e testa novamente;
    - Visto que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecido como:
    - Red;
    - Green;
    - Refactor
"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando')


felix = Gato('Felix')

felix.miar()

print(felix.nome)
