import math
import unittest


def solve_for_exp(a, b):
    return round(math.log(b, a))


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(5, solve_for_exp(4, 1024))
