import unittest


def profit(info):
    return round((info["sell_price"] - info["cost_price"]) * info["inventory"])


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual(14796, profit({
            "cost_price": 32.67,
            "sell_price": 45.00,
            "inventory": 1200
        }))
