import unittest

from robo import Robo


class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)
        print('setUp() sendo executado...')

    def test_carregar(self):
        """Testando se o robô está carregando a bateria"""
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        """Testando se o robô consegue dizer nome"""
        self.assertEqual(self.megaman.dizer_nome(), 'BEEP BOOP BEEP BOOP. EU SOU MEGA MAN.')
        self.assertEqual(self.megaman.bateria, 49, 'A bateria deveria estar em 49%')

    def tearDown(self):
        print('tearDown() sendo executado...')


if __name__ == '__main__':
    unittest.main()
