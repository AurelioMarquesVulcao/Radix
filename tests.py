import unittest
from ..api import api
from math import ceil
from math import trunc


# a formula de binet permite que eu encontre qualquer número fibonacci
def teste_fibonacci(n):
    t1 =0
    t2 =1
    cont = 3
    fibo = [t1, t2]
    while cont <= n+1:
        t3 = t1+t2
        t1 = t2
        t2 = t3
        cont += 1
        fibo.append(t3)
    return t3
print(teste_fibonacci(9))


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
# usando a formula de Binet para calcular qualquer termo de uma fibonacci

print("-"*90)
def binet(x):
    phi = 1.61803398874989
    n = ((phi**x) - (1 - phi)**x) / (5**.5)
    return ceil(n)


maximo2 = 2 * 4294967295
a=0
for c in range(0, 60):
    if binet(c) < maximo2:
        a = binet(c)
        b = c
print(a, b)




print("-"*60)


x = 49

phi = 1.61803398874989
n = ((phi**x) - (1 - phi)**x) / (5**.5)


#print(trunc(ceil(n)))
maximo = 4 * 65535
maximo2 = 2 * 4294967295
print(maximo)
print(maximo2)
print(trunc(ceil(n)) < maximo)
print(trunc(ceil(n)) < maximo2)


# if you want to unit test, with pytest remove the '#'
if __name__ == '__main__':
    unittest.main()
