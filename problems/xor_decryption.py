"""
Project Euler Problem 59: XOR Decryption

Each character on a computer is assigned a unique code and the
preferred standard is ASCII (American Standard Code for Information
Interchange). For example, uppercase A = 65, asterisk (*) = 42, and
lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to
ASCII, then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption
key on the cipher text, restores the plain text; for example, 65 XOR 42
= 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain
text message, and the key is made up of random bytes. The user would
keep the encrypted message and the encryption key in different
locations, and without both "halves", it is impossible to decrypt the
message.

Unfortunately, this method is impractical for most users, so the
modified method is to use a password as a key. If the password is
shorter than the message, which is likely, the key is repeated
cyclically throughout the message. The balance for this method is using
a sufficiently long password key for security, but short enough to be
memorable.

Your task has been made easy, as the encryption key consists of three
lower case characters. Using assets/p059_cipher.txt, a file containing
the encrypted ASCII codes, and the knowledge that the plain text must
contain common English words, decrypt the message and find the sum of
the ASCII values in the original text.
"""
import os
import string
import itertools
# ord('a') => 97, chr(97) => 'a'

def get_cipher(filepath):
    """
    Read the file containing the cipher and return
    it as a list. The filepath should be relative
    to the directory this file is located in
    """
    name_file_location = '/'.join([os.path.dirname(os.path.realpath(__file__)), filepath])
    with open(name_file_location, 'r') as f:
        text = f.read()

    cipher = [int(n) for n in text.split(',')]

    return cipher

def xor_decrypt(cipher, encryption_key):
    """
    Given the cipher and encryption key, decode the
    cipher and return the decrypted text.
    """
    # the key must be repeated to be the same length as the cipher
    remainder = len(cipher) % len(encryption_key)
    big_key = (len(cipher)//len(encryption_key)) * encryption_key
    if remainder > 0:
        # get enough of the encryption key to make the length
        # of the big key and the cipher equal
        big_key += encryption_key[:remainder]

    # make sure there weren't any errors expanding the encryption key
    assert len(big_key) == len(cipher)

    message = ''
    for k, c in zip(big_key, cipher):
        message += chr(c ^ ord(k))

    return message

if __name__ == '__main__':
    cipher = get_cipher('/assets/p059_cipher.txt')
    encryption_key = 'god'  # figure this out through eductated guesses
    text = xor_decrypt(cipher, encryption_key)

    # Sum the ASCII values of the decrypted text
    print(sum(ord(char) for char in text))
