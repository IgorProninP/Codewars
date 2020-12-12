"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
"""


# Solutions from Codewars:
#
# def move_zeros(arr):
#     l = [i for i in arr if isinstance(i, bool) or i!=0]
#     return l+[0]*(len(arr)-len(l))
#
# def move_zeros(array):
#     return sorted(array, key=lambda x: x == 0 and type(x) is not bool)
#

#
# def move_zeros(array):
#     return [a for a in array if isinstance(a, bool) or a != 0] + \
#            [a for a in array if not isinstance(a, bool) and a == 0]


def move_zeros(array):
    nulls = 0
    new_array = []
    for i in array:
        if i == 0 and type(i) != bool:
            nulls += 1
            continue
        else:
            new_array.append(i)
    new_array.extend(0 for _ in range(nulls))
    return new_array


if __name__ == '__main__':
    arr = [0, 1, None, 2, False, 1, 0, 1]
    print(move_zeros(arr))
