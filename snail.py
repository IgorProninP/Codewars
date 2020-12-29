"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element,
traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse
the 2-d array in a clockwise snail-shell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
"""


# Solutions from codewars:
#
# def snail(array):
#     import numpy as np
#     m = []
#     array = np.array(array)
#     while len(array) > 0:
#         m += array[0].tolist()
#         array = np.rot90(array[1:])
#     return m

# def snail(array):
#     if array:
#         top_row = list(array[0])
#         rotated_array = list(zip(*array[1:]))
#         rotated_array = rotated_array[::-1]
#         return top_row + snail(rotated_array)
#     else:
#         return []
#
# def snail(array):
#     out = []
#     while len(array):
#         out += array.pop(0)
#         array = list(zip(*array))[::-1] # Rotate
#     return out

def snail(snail_map):
    result = []

    while snail_map:
        result += snail_map.pop(0)
        if not snail_map:
            return result
        for i in snail_map:
            result.append(i.pop())
        for i in snail_map.pop().__reversed__():
            result.append(i)
        for i in reversed(snail_map):
            result.append(i.pop(0))

    return result


if __name__ == '__main__':
    three = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    four = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
    five = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]]

    print(snail(five))
