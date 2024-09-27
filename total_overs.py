import unittest


def total_overs(balls):
    remainder, overs = balls % 6, balls // 6
    if remainder == 0:
        return overs
    return float(str(overs) + "." + str(remainder))


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(400, total_overs(2400))
    def test_b(self):
        self.assertEqual(27.2, total_overs(164))