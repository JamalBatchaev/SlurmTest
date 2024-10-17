import unittest

import  isvalid

class IsValidTestCase(unittest.TestCase):
    def test_is_valid(self):
        self.assertTrue(isvalid.is_valid('()'))
        self.assertTrue(isvalid.is_valid('{}'))
        self.assertTrue(isvalid.is_valid('{[]}'))
    def test_is_invalid(self):
        self.assertFalse(isvalid.is_valid('('))
        self.assertFalse(isvalid.is_valid('{'))
        self.assertFalse(isvalid.is_valid('{[}]()'))

