import unittest
from exercises import element_search


class TestElementSearch(unittest.TestCase):
    def setUp(self):
        self.data = range(0, 10)

    def test_item_found(self):
        res = element_search.find(self.data, 9)
        self.assertTrue(res)

    def test_item_not_found(self):
        res = element_search.find(self.data, 19)
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()
   
