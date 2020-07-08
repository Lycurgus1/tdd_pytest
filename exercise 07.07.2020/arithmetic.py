import math

# Class for code to enable testing
class Artithmetic:
    # Creating static method so it can tested
    @staticmethod
    def find_sqrt(num):
        return math.sqrt(num)

    # Creating static method so it can tested
    @staticmethod
    def find_ceil(num):
        return math.ceil(num)

# HINT:- You can hard code the values in your tests using assert