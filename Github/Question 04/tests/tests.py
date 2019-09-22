import unittest
from ..api import api


class TestCrawler(unittest.TestCase):
    def test_01(self):
        self.assertEqual(api.fibonacci(3), test_01)


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


# insira o numero fibonacci que deseja testar
test_01 = teste_fibonacci(3)
test_02 = teste_fibonacci(4)
test_03 = teste_fibonacci(9)
test_04 = teste_fibonacci(7)
test_05 = teste_fibonacci(58)
test_06 = teste_fibonacci(59)
test_07 = teste_fibonacci(60)

if __name__ == '__main__':
    unittest.main()
