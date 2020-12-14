"""
Write a function that takes a string of braces, and determines if the order of the braces is valid.
It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and
curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
"""

# Solutions from codewars:
#
# def validBraces(string):
#     braces = {"(": ")", "[": "]", "{": "}"}
#     stack = []
#     for character in string:
#         if character in braces.keys():
#             stack.append(character)
#         else:
#             if len(stack) == 0 or braces[stack.pop()] != character:
#                 return False
#     return len(stack) == 0

"""
def validBraces(s):
    while '{}' in s or '()' in s or '[]' in s:
        s=s.replace('{}','')
        s=s.replace('[]','')
        s=s.replace('()','')
    return s==''
"""



def valid_braces(string):
    braces = list(string)
    ex = ('(]', '(}', '[)', '[}', '{)', '{]',)
    for exception in ex:
        if exception in string:
            return False
    for i in string:
        if i == '(' and ')' in braces[braces.index(i):]:
            braces.remove('(')
            braces.remove(')')
        elif i == '[' and ']' in braces[braces.index(i):]:
            braces.remove('[')
            braces.remove(']')
        elif i == '{' and '}' in braces[braces.index(i):]:
            braces.remove('{')
            braces.remove('}')
    return len(braces) == 0


if __name__ == '__main__':
    print(valid_braces('[({})]([])'))

