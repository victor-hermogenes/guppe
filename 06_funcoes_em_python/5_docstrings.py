"""
Documentando funções com Docstrings

OBS: Podemos ter acesso à documentaçãp de uma função em Python
utilizando a propriedade especial __doc__
"""

# Exemplos


def diz_oi():
    """Uma funcaoo simples que retorna a string 'Oi!'"""
    return 'Oi! '


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou o 'numero' à 'potencia'' informada.
    :param numero: Numero que desejamos gerar o exponencial.
    :param potencia: Potencia que queremos gerar o exponencial. Por padrao e 2
    :return: Retorna o expoencial de 'numero' por 'potencia'.
    """
    return numero ** potencia
