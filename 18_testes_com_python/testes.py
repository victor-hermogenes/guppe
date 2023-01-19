import unittest


from atividades import comer, dormir, e_engracada


class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        """Testando o retorndo com comida gostosa"""
        self.assertEqual(
            comer(comida='pizza', e_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Puts, dormi muito... Estou atrasado para o trabalho.'
        )

    def test_e_engracada(self):
        """Testando se a pessoa é engraçada"""
        self.assertEqual(e_engracada('Sérgio Malandro'), False)
        self.assertFalse(e_engracada('Sérgio Malandro'))
        self.assertTrue(e_engracada('Jim Carrey'), 'jim Carrey deveria ser engraçado')


if __name__ == '__main__':
    unittest.main()
