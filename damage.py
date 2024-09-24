import math
import unittest


def damage(damage, speed, time):
    base = damage * speed
    if base == 0 or damage < 0 or speed < 0:
        return "invalid"

    if time == "second":
        return base
    elif time == "minute":
        return base * 60
    elif time == "hour":
        return base * 60 * 60


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(200, damage(40, 5, "second"))

    def test_b(self):
        self.assertEqual(6000, damage(100, 1, "minute"))

    def test_c(self):
        self.assertEqual(720000, damage(2, 100, "hour"))
