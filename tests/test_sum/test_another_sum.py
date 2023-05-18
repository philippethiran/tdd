import unittest
from sum.another_sum import another_sum, add_10

class MyTestCase(unittest.TestCase):
    def test_another_sum(self):
        assert another_sum(3, 2) == 5

    def test_add_3(self):
        assert add_10(3) == 13
        
   def test_add_neg(self):
        assert add_10(-3) == 7

if __name__ == '__main__':
    unittest.main()
