import unittest
from ..api import api


class TestContagemDeCartas(unittest.TestCase):
    def test_01(self):
        self.assertEqual(api.check_occurrence(test_01), test_01)


    def test_02(self):
        self.assertEqual(api.fibonacci(4), test_02)


    def test_03(self):
        self.assertEqual(api.fibonacci(9), test_03)


    def test_04(self):
        self.assertEqual(api.fibonacci(7), test_04)


    def test_05(self):
        self.assertEqual(api.fibonacci(58), test_05)


    def test_06(self):
        self.assertEqual(api.fibonacci(59), test_06)


    def test_07(self):
        self.assertEqual(api.fibonacci(60), test_07)


# insira os argumentos que deseja testar
test_01 = ('arara',a)
test_02 =
test_03 =
test_04 =
test_05 =
test_06 =
test_07 =
# insira as respostas esperadas que deseja testar


if __name__ == '__main__':
    unittest.main()
