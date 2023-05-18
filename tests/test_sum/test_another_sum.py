import unittest
from sum.another_sum import another_sum, add_10, add_serie, add_even_serie

class MyTestCase(unittest.TestCase):
    def test_another_sum(self):
        assert another_sum(3, 2) == 5

    def test_add_10(self):
        assert add_10(3) == 13
        
    def test_add_neg(self):
        assert add_10(-3) == 7

    def test_add_serie(self):
        assert add_serie(3, 5) == 12

    def test_add_event_serie(self):
        assert add_even_serie(3, 5) == 4
        assert add_even_serie(2, 5) == 6
        assert add_even_serie(2, 6) == 12
        assert add_even_serie(-1, 6) == 12

if __name__ == '__main__':
    unittest.main()
