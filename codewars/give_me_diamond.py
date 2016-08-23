# http://www.codewars.com/kata/5503013e34137eeeaa001648/train/python


def diamond(n):
    if n < 1 or n % 2 == 0:
        return None
    diamond_list = ['*' * n, ]
    for i in range(n - 2, 0, -2):
        row = ' ' * ((n - i) // 2) + '*' * i
        diamond_list.insert(0, row)
        diamond_list.append(row)
    return '\n'.join(diamond_list) + '\n'
