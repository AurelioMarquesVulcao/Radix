import unittest
from form_generator import random_start_date
from form_generator import random_end_date


class TestApi(unittest.TestCase):
    def test_01(self):
        self.assertEqual(test_01(), 'ok')


    def test_02(self):
        self.assertEqual(0, 0)


    def test_03(self):
        self.assertEqual(0, 0)


    def test_04(self):
        self.assertEqual(0, 0)


    def test_05(self):
        self.assertEqual(0, 0)


    def test_06(self):
        self.assertEqual(0, 0)


    def test_07(self):
        self.assertEqual(0, 0)


def test_01():
    try:
        for c in range(50000):
            random_start_date()
        a = 'ok'
    except:
        a = 'False'
    return a


if __name__ == '__main__':
    unittest.main()
