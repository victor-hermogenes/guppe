"""
POO - Classes

Em POO, classes nada mais são que modelos dos objetos do mundo real representados computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
    - Atributos -> Representam as características do objeto. Ou seja, pelos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente
    iríamos querer saber se a lâmpada é 110 ou 220 volts, se ela é branca, amarela, vermelha ou
    outra cor, qual é a luminosidade dela e etc.

    - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que ele
    pode realizar no seusistema. No caso da lâmpada, por exemplo, um comportamento comum
    que muito provavelmente iríamos querer representar no nosso sistema, é o de ligar e desligar
    ela.

Em Python, para definir uma classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está
implementado.

OBS: Quando nomeamos nossas classes em Python utilizamos por convenção o nome com incial
em maiúsculo. Se o nome for composto, utiliza-se as iniciais de ambas as palavras em
maiúsculo, todas juntas.

Dica Geek: Em computação não utilizamos: Acentuação, caracteres especiais, espaços ou similares
para nomes de classes, atributos, arquivos, diretórios e etc.

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos
estes objetos qe serão mapeados para classes de entidade.
"""


class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


class Int:
    pass


valor = int('42')    # cast

print(help(int))

inteiro = Int()
