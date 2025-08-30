'''
Author: Scott Field
Version: 1.00
Date: 4/17/2023
Program Name: test_sum_unittest
Program Purpose: practice code testing using the unittest library
'''
#import library
import unittest

#Test Cases
class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

#Main Loop
if __name__ == '__main__':
    unittest.main()