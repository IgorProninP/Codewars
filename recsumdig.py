"""
Given n, take the sum of the digits of n. If that value has more than one digit,
continue reducing in this way until a single-digit number is produced. The input
will be a non-negative integer.
"""


# best solutions from codewars:
# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))
#
# def digital_root(n):
#     return n%9 or n and 9
################################################################


def digital_root(num):
    sum_digits = sum(int(digit) for digit in str(num))
    if sum_digits < 10:
        return sum_digits
    return digital_root(sum_digits)


if __name__ == '__main__':
    number = int(input('Enter a number: '))
    print(digital_root(number))
