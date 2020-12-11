"""
Square every digit of a number. For example, if we run 9119 through the function,
811181 will come out, because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer
"""


def square_digits(num):
    return str(''.join(str(int(x) ** 2) for x in str(num)))


if __name__ == '__main__':
    print(square_digits(input('Enter a number: ')))
