import unittest
from api import winner_is


class TestApi(unittest.TestCase):
    def test_01(self):
        self.assertEqual(winner_is('tesoura', 'papel'), 'Bazinga!')

    def test_02(self):
        self.assertEqual(winner_is('papel', 'pedra'), 'Bazinga!')

    def test_03(self):
        self.assertEqual(winner_is('pedra', 'lagarto'), 'Bazinga!')

    def test_04(self):
        self.assertEqual(winner_is('lagarto', 'Spock'), 'Bazinga!')

    def test_05(self):
        self.assertEqual(winner_is('Spock', 'tesoura'), 'Bazinga!')

    def test_06(self):
        self.assertEqual(winner_is('tesoura', 'lagarto'), 'Bazinga!')

    def test_07(self):
        self.assertEqual(winner_is('lagarto', 'papel'), 'Bazinga!')

    def test_08(self):
        self.assertEqual(winner_is('papel', 'Spock'), 'Bazinga!')

    def test_09(self):
        self.assertEqual(winner_is('Spock', 'pedra'), 'Bazinga!')

    def test_10(self):
        self.assertEqual(winner_is('pedra', 'tesoura'), 'Bazinga!')

    def test_11(self):
        self.assertEqual(winner_is('pedra', 'papel'), 'Raj trapaceou')

    def test_12(self):
        self.assertEqual(winner_is('Spock', 'Spock'), 'De novo!')

    def test_13(self):
        self.assertEqual(winner_is('lagarto', 'tesoura'), 'Raj trapaceou')



if __name__ == '__main__':
    unittest.main()
