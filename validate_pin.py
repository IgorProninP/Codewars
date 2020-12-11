"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but
exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
"""


# Solutions from Codewar:
#
# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()
#
#############################################################################


def validate_pin(pin):
    for i in pin:
        if not i.isdigit():
            return False
    return True if len(pin) == 4 or len(pin) == 6 else False


if __name__ == '__main__':
    print(validate_pin('312345'))
