import unittest
from api import api


# insira os argumentos que deseja testar
test_01 = ('arara', 'a')
answer_01 = 3
test_02 = 0
answer_02 = 0
test_03 = 0
answer_03 = 0
test_04 = 0
answer_04 = 0
test_05 = 0
answer_05 = 0
test_06 = 0
answer_06 = 0
test_07 = 0
answer_07 = 0

class TestContagem(unittest.TestCase):
    def test_01(self):
        self.assertEqual(api.check_occurrence('arara', 'a'), '3')


    '''def test_02(self):
        self.assertEqual(api.check_occurrence(test_01),answer_01)


    def test_03(self):
        self.assertEqual(api.check_occurrence(test_01),answer_01)


    def test_04(self):
        self.assertEqual(api.check_occurrence(test_01),answer_01)


    def test_05(self):
        self.assertEqual(api.check_occurrence(test_01),answer_01)


    def test_06(self):
        self.assertEqual(api.check_occurrence(test_01),answer_01)


    def test_07(self):
        self.assertEqual(api.check_occurrence(test_01),answer_01)'''




if __name__ == '__main__':
    unittest.main()
