import unittest
from sum.another_sum import another_sum

class MyTestCase(unittest.TestCase):
    def test_another_sum(self):
        assert another_sum(3, 2) == 5

if __name__ == '__main__':
    unittest.main()
