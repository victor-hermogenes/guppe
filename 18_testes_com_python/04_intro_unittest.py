"""
Introdução ao módulo Unittest

Unittest → Testes unitários

O que são testes unitários?

Teste unitário é a forma de se testar unidades individuais de código-fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos, etc.

#OBS: Teste unitário não é específico a linguagem Python.

Para criar os nossos testes, criamos classes que herdam unittest TestCase
e a partir de então ganhamos todos os 'assertions' presentons no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Casos de testes para sua unidade.

# Conhecendo assertions:

Método:
assertEqual(a, b)             a == b
asserNotEqual(a, b)           a != b
assertTrue(x)                 x é verdadeiro
assertFalse(x)                x é falso
assertIs(a, b)                a é b
asserIsNot(a, b)              a não é b
assertIsNone(x)               x é None
assertIsNotNone(x)            x não é None
assertIn(a, b)                a está em b
assertNotIn(a, b)             a não está em b
assertIsInstance(a, b)        a é instância de b
assertNotIsInstance(a, b)      a não é instância de b

Por convenção, todos os testes em um test case, devem ter o seu nome
e iniciado em test_

# Para executar os testes com unitterst

python nome_do_modulo.py

# Para executar os testes com unittest no modo verbose

python nome_do_modulo.py -v

# Docstrings nos testes

Podemos acrescentar (é recomendado) docstrings nos nossos testes.
"""

# Prática
