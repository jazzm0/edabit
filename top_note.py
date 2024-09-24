import unittest


def top_note(student):
    return {"name": student["name"], "top_note": max(student["notes"])}


class TestStringMethods(unittest.TestCase):
    def test_a(self):
        self.assertEqual({"name": "John", "top_note": 5}, top_note({"name": "John", "notes": [3, 5, 4]}))
