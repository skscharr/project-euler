"""
Project Euler Problem 22: Names Scores
https://projecteuler.net/problem=22

Using assets/p022_names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import os
import string

def get_names(filepath):
    """
    Read the file containing the names and return
    it as a list. The filepath should be relative
    to the directory this file is located in
    """
    name_file_location = '/'.join([os.path.dirname(os.path.realpath(__file__)), filepath])
    with open(name_file_location, 'r') as f:
        text = f.read()

    # get rid of double quotes before creating the list,
    # otherwise you'll end up with '"NAME"'
    scrubbed_text = text.replace('"', '')
    names_list = scrubbed_text.split(',')

    return names_list

def names_scores(names):
    """
    Given a list of names, sort them into alphabetical order
    and then calculate its score by adding together the letter
    score (i.e. A=1, B=2, etc.) and then multiplying that sum by the
    position of the name in the list (i.e. first name in the list
    would be sum * 1, second name sum * 2, etc.)

    All the individual name scores will be summed and that total
    will be returned.
    """
    # create a dictionary to store the letter scores
    score_dict = {
        char: idx+1 for idx, char in enumerate(string.ascii_uppercase)
    }
    sorted_names = sorted(names)

    total_name_score = 0
    for idx, name in enumerate(sorted_names):
        name_sum = sum(score_dict[char] for char in name)
        total_name_score += name_sum * (idx + 1)

    return total_name_score

if __name__ == '__main__':
    names = get_names('assets/p022_names.txt')
    print(names_scores(names))
