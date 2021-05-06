import unittest

from intro_tkinter import add_two_numbers
from intro_tkinter import subtract_two_numbers


class TestMyMaths(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(2,2), 4, "Adding two numbers failed")

    def test_subtract_two_numbers(self):
        self.assertEqual(subtract_two_numbers(2, 2), 0, "Subtracting two numbers")