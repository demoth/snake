from unittest.case import TestCase
from main import Screen

class TestScreen(TestCase):

    def test_set_get_method(self):
        s = Screen(10, 10)
        self.assertEqual(s[(5, 5)], ' ')
        s[(5, 5)] = '#'
        self.assertEqual(s[(5, 5)], '#')
        self.assertEqual(s.cells[(5, 5)], '#')