"""
Project Euler Problem 112: Bouncy Numbers
https://projecteuler.net/problem=112

Working from left-to-right if no digit is exceeded by the digit
to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is
called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor
decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but
just over half of the numbers below one-thousand (525) are bouncy.
In fact, the least number for which the proportion of bouncy numbers
first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the
time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is
exactly 99%.
"""

def find_bouncy_percentage(pct):
    """
    Given a percentage (pct), calculate the least number
    for which the proportion of bouncy numbers equals
    that percentage.

    For example, to find the number where the proportion
    first reaches 50%:
        find_bouncy_percentage(50)
    """
    bouncy_total = 0
    current_num = 1

    while (bouncy_total/current_num) * 100 < pct:
        increasing = False
        decreasing = False
        str_num = str(current_num)
        for i in range(len(str_num)):
            if i == (len(str_num) - 1):
                # break from loop otherwise we'll get an IndexError
                break
            if int(str_num[i]) < int(str_num[i+1]):
                increasing = True
            if int(str_num[i]) > int(str_num[i+1]):
                decreasing = True
            if increasing and decreasing:
                # increase the total and break because we don't
                # need to keep going if we meet the criteria
                bouncy_total += 1
                break
        current_num += 1
    return current_num, bouncy_total, (bouncy_total/current_num) * 100

if __name__ == '__main__':
    print(find_bouncy_percentage(99))
