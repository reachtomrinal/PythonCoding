import unittest
from app.calc import add


class TestModule(unittest.TestCase):
    """ test module to verify the calculator app is working as expected """

    def test_addInteger(self):
        """ verify the addition of two Integers """
        self.assertEqual(add(3, 5), 8)

    def test_addNonDigit(self):
        """ Add non digit values should return false"""
        self.assertFalse(add(3, 'u'))

