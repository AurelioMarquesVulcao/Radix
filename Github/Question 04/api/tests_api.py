import unittest
from .api import check_occurrence


class TestContagem(unittest.TestCase):
    # do teste 01 ao 25 testei se o dicionário funcionava
    def test_01(self):
        self.assertEqual(check_occurrence('arara', 'a'), 3)

    def test_02(self):
        self.assertEqual(check_occurrence('arara', 'b'), 0)

    def test_03(self):
        self.assertEqual(check_occurrence('arara', 'c'), 0)

    def test_04(self):
        self.assertEqual(check_occurrence('arara', 'd'), 0)

    def test_05(self):
        self.assertEqual(check_occurrence('arara', 'f'), 0)

    def test_06(self):
        self.assertEqual(check_occurrence('arara', 'g'), 0)

    def test_07(self):
        self.assertEqual(check_occurrence('arara', 'h'), 0)

    def test_08(self):
        self.assertEqual(check_occurrence('arara', 'i'), 0)

    def test_09(self):
        self.assertEqual(check_occurrence('arara', 'j'), 0)

    def test_10(self):
        self.assertEqual(check_occurrence('arara', 'k'), 0)

    def test_11(self):
        self.assertEqual(check_occurrence('arara', 'l'), 0)

    def test_12(self):
        self.assertEqual(check_occurrence('arara', 'm'), 0)

    def test_13(self):
        self.assertEqual(check_occurrence('arara', 'n'), 0)

    def test_14(self):
        self.assertEqual(check_occurrence('arara', 'o'), 0)

    def test_15(self):
        self.assertEqual(check_occurrence('arara', 'p'), 0)

    def test_16(self):
        self.assertEqual(check_occurrence('arara', 'q'), 0)

    def test_17(self):
        self.assertEqual(check_occurrence('arara', 'r'), 2)

    def test_18(self):
        self.assertEqual(check_occurrence('arara', 's'), 0)

    def test_19(self):
        self.assertEqual(check_occurrence('arara', 't'), 0)

    def test_20(self):
        self.assertEqual(check_occurrence('arara', 'u'), 0)

    def test_21(self):
        self.assertEqual(check_occurrence('arara', 'v'), 0)

    def test_22(self):
        self.assertEqual(check_occurrence('arara', 'x'), 0)

    def test_23(self):
        self.assertEqual(check_occurrence('arara', 'z'), 0)

    def test_24(self):
        self.assertEqual(check_occurrence('arara', 'y'), 0)

    def test_25(self):
        self.assertEqual(check_occurrence('arara', 'w'), 0)

    def test_26(self):
        self.assertEqual(check_occurrence('arara', 'a'), 3)

    def test_27(self):
        self.assertEqual(check_occurrence('arara', 'a'), 3)

    def test_28(self):
        self.assertEqual(check_occurrence('arara', 'a'), 3)

    def test_29(self):
        self.assertEqual(check_occurrence('arara', 'a'), 3)

    def test_30(self):
        self.assertEqual(check_occurrence('arara', 'a'), 3)

    def test_31(self):
        self.assertEqual(check_occurrence('arara', 'a'), 3)

    def test_32(self):
        self.assertEqual(check_occurrence('arara', 'a'), 3)


if __name__ == '__main__':
    unittest.main()
