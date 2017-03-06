"""
Unit tests for xor_decryption.py
"""
import unittest

from problems.xor_decryption import get_cipher, xor_decrypt

class XORDecryptionTests(unittest.TestCase):
    def test_get_cipher(self):
        """
        Test get_cipher() returns the expected list
        """
        expected_cipher = [
            42, 65, 24, 12, 23, 17, 67, 2, 21, 23, 18, 85, 67, 40, 84,
            20, 0, 26, 23, 65, 0, 12, 65, 4, 6, 21, 84, 2, 13, 24, 67,
            21, 28, 6, 65, 23, 2, 21, 7, 67, 8, 26, 67, 21, 28, 6, 65,
            3, 12, 19, 24, 7, 79, 84, 42, 65, 3, 10, 18, 28, 67, 4, 2,
            6, 19, 13, 67, 2, 21, 23, 65, 23, 12, 20, 24, 7, 65, 22, 6,
            65, 25, 26, 65, 18, 17, 8, 17, 13, 5, 90, 67, 44, 49, 44,
            54, 85]

        cipher = get_cipher('assets/test_cipher.txt')

        self.assertEqual(cipher, expected_cipher)

    def test_xor_decript(self):
        """
        Test xor_decrypt() returns the expected text
        """
        expected_text = 'I love cats! I want to pet all the cats in the world. I wish every cat could be my friend. MEOW!'
        encryption_key = 'cat'

        text = xor_decrypt(
            get_cipher('assets/test_cipher.txt'), encryption_key)

        self.assertEqual(text, expected_text)
