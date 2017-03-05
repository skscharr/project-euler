"""
Unit tests for names_scores.py

These tests use the file assets/test_names.txt
"""
import unittest

from problems.names_scores import get_names, names_scores

class NameScoresTests(unittest.TestCase):
    def test_get_names(self):
        """
        Test get_names() returns the list expected list of names
        """
        expected_list = [
            'CATHY', 'JOANN', 'LORRAINE', 'SALLY', 'REGINA', 'ERICA',
            'BEATRICE', 'DOLORES', 'AUDREY', 'YVONNE'
        ]

        names_list = get_names('assets/test_names.txt')

        self.assertEqual(names_list, expected_list)

    def test_names_scores(self):
        """
        Test names_scores() correctly calculates the score
        """
        names = [
            'CATHY',  # (3 + 1 + 20 + 8 + 25) = 57
            'JOANN',  # (10 + 15 + 1 + 14 + 14) = 54
            'ERICA'   # (5 + 18 + 9 + 3 + 1) = 36
        ]

        # cathy(57)*1 + erica(36)*2 + joann(54)* 3 == 57 + 72 + 162
        expected_total_score = 291

        total_score = names_scores(names)

        self.assertEqual(total_score, expected_total_score)
