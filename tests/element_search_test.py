import unittest
from exercises import element_search


class TestElementSearch(unittest.TestCase):
    def setUp(self):
        self.data = range(0, 10)

    def test_item_found(self):
        res = element_search.find(self.data, 3)
        self.assertTrue(res)

    def test_item_not_found(self):
        res = element_search.find(self.data, 19)
        self.assertFalse(res)

    def test_item_found_unsorted(self):
        res = element_search.find([9,2,3,4,1,4,42], 9)
        self.assertTrue(res)        

if __name__ == '__main__':
    unittest.main()
   
