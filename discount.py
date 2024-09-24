import unittest


def dis(price, discount):
    return price * ((100 - discount) / 100)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(750, dis(1500, 50))
