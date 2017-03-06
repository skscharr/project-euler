"""
Unit tests for lexographic_permutations.py
"""
import unittest
import itertools

from problems.lexographic_permutations import (
    lexo_permutations,
    get_permutation_at_index
)

class LexographicPermutationsTests(unittest.TestCase):
    def test_lexo_permutations(self):
        """
        Test lexo_permutations() generates permutations as expected
        """
        expected_perms = ['012', '021', '102', '120', '201', '210']
        perms = lexo_permutations('012')
        self.assertEqual(perms, expected_perms)

    def test_lexo_permutations_vs_standard_lib(self):
        """
        Test permutations function returns the same as what the
        standard lib `itertools.permutations()` does
        """
        perms = lexo_permutations('012')
        sl_perms = [
            ''.join(str(i) for i in perm)
            for perm in itertools.permutations('012')
        ]

        self.assertEqual(perms, sl_perms)

    def test_get_permutation_at_index(self):
        """
        Test we get back the expected value at a given index
        """
        self.assertEqual(get_permutation_at_index('012', 3), '120')
        self.assertEqual(get_permutation_at_index('012', 0), '012')
        self.assertEqual(
            get_permutation_at_index('012', 8),
            'Error! Index 8 is out of range. 012 generated 6 permutations'
        )
