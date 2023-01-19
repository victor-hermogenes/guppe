"""
Unittest - Antes e após hooks

----
hooks - são os testes em si. Ou seja, a execução dos testes.
----

setup -> É executado antes de cada método de teste. É útil para criarmos instâncias de objetos e outros dados;

tearDown() -> É executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões com
bancos de dados.


"""

import unittest

class Modulotest(unittest.TestCase):

    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeiro(self):
        # setUp() vai rodar antes do teste.
        # tearDown() vai rodar após o teste.
        pass

    def test_segundo(self):
        # setUp() vai rodar antes do teste.
        # tearDown() vai rodar após o teste.
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass
    