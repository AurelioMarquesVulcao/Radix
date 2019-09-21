import unittest


class TestCrawler(unittest.TestCase):
    def test_01(self):
        self.assertEqual(1, test_01)


# insert title of page do you need test.
test_01 = 1


# if you want to unit test, with pytest remove the '#'
if __name__ == '__main__':
    unittest.main()
