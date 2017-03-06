"""
Project Euler Problem 24: Lexographic Permutations
https://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects. For example, 3124
is one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2,
3, 4, 5, 6, 7, 8 and 9?
"""

def lexo_permutations(num_str):
    """
    Given a string of integers, generate all lexicographic
    permutations.
    """
    if len(num_str) <= 1:
        return num_str

    permutations = list()

    for i in range(len(num_str)):
        for n in lexo_permutations(num_str[:i] + num_str[i+1:]):
            permutations.append(num_str[i] + n)
    return permutations


def get_permutation_at_index(num_str, idx):
    """
    Given a list of integers as a string (i.e. '012') and an
    index, generate all permutations for the list and then
    retrieve the item at the given index.

    We are looking at the integers as individual characters
    so it's easier to parse it like a string rather than a list
    of integers
    """
    permutations = lexo_permutations(num_str)

    try:
        return permutations[idx]
    except IndexError:
        return (
            'Error! Index {} is out of range. {} generated '
            '{} permutations'.format(
                idx, num_str, len(permutations)
            )
        )

if __name__ == '__main__':
    num_str = '0123456789'
    # with the first item at index 0, index 999999 will
    # be the millionth item
    idx = 999999
    print(get_permutation_at_index(num_str, idx))
