#!/usr/bin/python
"""
tests for 6-max_integer
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ tests for max_integer"""
    def test_def(self):
        """tests for normal input"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_none(self):
        """tests for empty input"""
        self.assertEqual(max_integer(), None)

    def test_neg(self):
        """tests for negative"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_neg_pos(self):
        """tests for composed input"""
        self.assertEqual(max_integer([1, -4, -5, 5, 3]), 5)

    def test_non_int(self):
        """tests for non-integer input"""
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3])

    def test_float(self):
        """tests for float"""
        self.assertEqual(max_integer([1, 2, 3.3]), 3.3)

if __name__ == "__main__":
    unittest.main()
