"""
Unit tests for bouncy_numbers.py
"""
import unittest

from problems.bouncy_numbers import find_bouncy_percentage

class BouncyNumbersTests(unittest.TestCase):
    def test_find_bouncy_percentage(self):
        """
        Test find_bouncy_percentage() returns the expected
        answer for known scenarios
        """
        pct_50, _, _ = find_bouncy_percentage(50)

        self.assertEqual(pct_50, 538)

        pct_90, _, _ = find_bouncy_percentage(90)

        self.assertEqual(pct_90, 538)
