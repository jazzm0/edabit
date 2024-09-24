import unittest


def how_many_seconds(hours):
    return 60 * 60 * hours


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(7200, how_many_seconds(2))
