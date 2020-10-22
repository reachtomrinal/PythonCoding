import unittest
from anagram.anagram import anagram


class Test_anagram(unittest.TestCase):
    """ Class is to verify the anagram """

    def test_ifAnagram(self):
        """ verify the happy path """
        # str1, str1 = "binary", "brainy"
        self.assertTrue(anagram("binary", "brainy"))


        #------------------------------ Negative scenarios ---------------------------------------------

    def test_notAnagram(self):
        """ verify for negative value """
        self.assertFalse(anagram("text", "abcd"))

    def test_notAnagramEmptyValue(self):
        """ negative scenarios for empty value """
        self.assertFalse(anagram("", "xyz"))

    def test_moreThanOneChar(self):
        """ verify when more than one char """
        self.assertFalse(anagram("aaab", "ab"))



