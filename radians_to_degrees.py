import math
import unittest


def radians_to_degrees(rad):
    return round(((180 * rad) / math.pi), 1)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(57.3, radians_to_degrees(1))
