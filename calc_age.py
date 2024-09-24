import unittest


def calc_age(age):
    return 365 * age


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(23725, calc_age(65))
