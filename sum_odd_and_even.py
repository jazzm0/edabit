import unittest


def sum_odd_and_even(lst):
    odd, even = 0, 0
    for n in lst:
        if n % 2 == 0:
            even += n
        else:
            odd += n
    return [even, odd]


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual([12, 9], sum_odd_and_even([1, 2, 3, 4, 5, 6]))
