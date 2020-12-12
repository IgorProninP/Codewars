"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts,
pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names
of people who like an item. It must return the display text as shown in the examples:
"""


# Solutions from Codewars:
#
# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this',
#         2: '{} and {} like this',
#         3: '{}, {} and {} like this',
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)

################################################################


def likes(names):
    one_likes = '{} likes this'
    two_like = '{} and {} like this'
    three_like = '{}, {} and {} like this'
    many_like = '{}, {} and {} others like this'
    if not names:
        return one_likes.format('no one')
    elif len(names) == 1:
        return one_likes.format(*names)
    elif len(names) == 2:
        return two_like.format(*names)
    elif len(names) == 3:
        return three_like.format(*names)
    else:
        return many_like.format(*names[:2], len(names) - 2)


if __name__ == '__main__':
    print(likes(['John', 'Alex', 'Max', 'Bob']))
