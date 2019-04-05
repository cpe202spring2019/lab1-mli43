import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

        tlist = [1]
        self.assertEqual(max_list_iter(tlist), 1)

        tlist = [3, 2, 5]
        self.assertEqual(max_list_iter(tlist), 5)

        tlist = [2.5, 3.7, 0]
        self.assertAlmostEqual(max_list_iter(tlist), 3.7)

        tlist = [4, 4]
        self.assertEqual(max_list_iter(tlist), 4)





"""    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 ) """

if __name__ == "__main__":
        unittest.main()

    
