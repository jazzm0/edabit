import unittest


def fizz_buzz(num):
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual("Fizz", fizz_buzz(3))

    def test_b(self):
        self.assertEqual("Buzz", fizz_buzz(5))

    def test_c(self):
        self.assertEqual("FizzBuzz", fizz_buzz(15))

    def test_d(self):
        self.assertEqual("4", fizz_buzz(4))
