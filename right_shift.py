import unittest
from math import floor


def shift_to_right(x, y):
    return floor(x / 2 ** y)
    # return int(str(bin(x))[0:-y], 2)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(10, shift_to_right(80, 3))

    def test_b(self):
        self.assertEqual(-6, shift_to_right(-24, 2))

    def test_c(self):
        self.assertEqual(-3, shift_to_right(-5, 1))
