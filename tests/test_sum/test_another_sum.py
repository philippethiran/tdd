import unittest
from sum.another_sum import another_sum, adD10

class MyTestCase(unittest.TestCase):
    def test_another_sum(self):
        assert another_sum(3, 2) == 5

    def test_one10(self):
        assert adD10(3) == 13

if __name__ == '__main__':
    unittest.main()
