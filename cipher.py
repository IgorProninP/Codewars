"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13
letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be
returned as they are. Only letters from the latin/english alphabet should be shifted,
like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""


def rot13(message):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    upper_alphabet = lower_alphabet.upper()
    cipher = ''
    for letter in message:
        if letter in lower_alphabet:
            cipher += lower_alphabet[lower_alphabet.find(letter):][13]
        elif letter in upper_alphabet:
            cipher += upper_alphabet[upper_alphabet.find(letter):][13]
        else:
            cipher += letter

    return cipher


if __name__ == '__main__':
    print(rot13('Test'))
