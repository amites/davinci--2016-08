#!/usr/bin/python

"""
Solution to
    http://www.codewars.com/kata/5503013e34137eeeaa001648/train/python
"""

def diamond(n):
    if n < 1 or n % 2 == 0:
        return None
    diamond_list = ['*' * n, ]
    for i in range(n - 2, 0, -2):
        row = ' ' * ((n - i) // 2) + '*' * i
        diamond_list.insert(0, row)
        diamond_list.append(row)
    return '\n'.join(diamond_list) + '\n'


def test_diamond():
    diamond_string = diamond(3)
    correct_answer = ''.join([' *\n', '***\n', ' *\n'])
    if diamond_string != correct_answer:
        print 'diamond is broken'
        print 'diamond returned:'
        print diamond_string
        print 'diamond should have returned:'
        print correct_answer
