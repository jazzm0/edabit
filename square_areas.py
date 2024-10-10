import unittest


def square_areas_difference(r):
    return 2 * r ** 2


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(50, square_areas_difference(5))

    def test_b(self):
        self.assertEqual(72, square_areas_difference(6))
