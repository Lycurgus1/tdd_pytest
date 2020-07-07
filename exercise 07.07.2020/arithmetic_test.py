import pytest
import unittest
import math

from arithmetic import Artithmetic

class Arithmetic_test(unittest.TestCase):

    easy_calc = Artithmetic()

    def test_find_sqrt(self):
        self.assertEqual(self.easy_calc.find_sqrt(16), 4)

    def test_find_ceil(self):
        self.assertEqual(self.easy_calc.find_ceil(1.4), 2)

calc = Artithmetic
print(calc.find_sqrt(16))
print(calc.find_ceil(25.98450754))