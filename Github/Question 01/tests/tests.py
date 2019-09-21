import unittest
from ..api import api
from math import ceil


# a formula de binet permite que eu encontre qualquer número fibonacci
def binet(x):
    phi = 1.61803398874989
    n = ((phi**x) - (1 - phi)**x) / (5**.5)
    return ceil(n)


class TestCrawler(unittest.TestCase):
    def test_01(self):
        self.assertEqual(api.fibonacci(), test_01)


    def test_02(self):
        self.assertEqual(api.fibonacci(), test_02)


    def test_03(self):
        self.assertEqual(api.fibonacci(), test_03)


    def test_04(self):
        self.assertEqual(api.fibonacci(), test_04)


    def test_05(self):
        self.assertEqual(api.fibonacci(), test_05)


    def test_06(self):
        self.assertEqual(api.fibonacci(), test_06)


    def test_07(self):
        self.assertEqual(api.fibonacci(), test_07)


# insira o numero fibonacci que deseja testar
test_01 = binet(0)
test_02 = binet(4)
test_03 = binet(2)
test_04 = binet(7)
test_05 = binet(58)
test_06 = binet(59)
test_07 = binet(60)
# usando a formula de Binet para calcular qualquer termo de uma fibonacci


# if you want to unit test, with pytest remove the '#'
if __name__ == '__main__':
    unittest.main()
