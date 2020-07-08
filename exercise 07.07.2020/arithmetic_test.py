# Importing relevant modules
import pytest
import unittest

# Importing class from the arithmetic file
from arithmetic import Arithmetic

# Creating class
class Arithmetic_Test(unittest.TestCase):

    # Creating class object
    easy_calc = Arithmetic()

    # Creating test method for the find_sqrt function
    def test_find_sqrt(self):
        self.assertEqual(self.easy_calc.find_sqrt(25), 5)

    # Creating test method for the find_sqrt function
    def test_find_ceil(self):
        self.assertEqual(self.easy_calc.find_ceil(1.4), 2)

# # Testing method
# # calc = Artithmetic()
# # print(calc.find_sqrt(25))
# print(calc.find_ceil(1.451231))