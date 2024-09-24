import unittest


def cubes(a):
    return a ** 3


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(125, cubes(5))
