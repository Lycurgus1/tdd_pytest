import pytest
import unittest
import math

from code import *

class Code_Test(unittest.TestCase):

    easy_calc = Code()

    def test_find_sqrt(self):
        self.assertEqual(self.easy_calc.find_sqrt(2), 4)

    def test_find_ceil(self):
        self.assertEqual(self.easy_calc.find_ceil(1.4), 2)