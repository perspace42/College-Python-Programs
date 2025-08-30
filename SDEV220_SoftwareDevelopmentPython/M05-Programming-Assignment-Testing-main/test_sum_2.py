'''
Author: Scott Field
Version: 1.00
Date: 4/17/2023
Program Name: test_sum_2
Program Purpose: Practice and implement code testing practices.
'''

#test if the sum of numbers is equal to 6, then output an error message if not
def test_sum():
    assert sum([1,2,3]) == 6, "Should be 6"

#test if the sum of numbers (within a tuple) is equal to 6, then output an error message if not
def test_sum_tuple():
    assert sum((1,2,2)) == 6, "Should be 6"

#main loop
if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    #If any assert statement fails execution stops and the print statement will not execute
    print("Everything Passed")