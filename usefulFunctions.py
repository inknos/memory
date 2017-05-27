import commonVar as common


def vprint(*args, sep=' ', end='\n', file=None):
    if common.verbose is True:
        print(*args, sep=' ', end='\n', file=None)


def digit_input(DEFAULT=1, msg=""):
    input_str = input(msg)
    if len(input_str) == 0:
        pass
    elif not input_str.isdigit():
        pass
    else:
        try:
            DEFAULT = eval(input_str)
        except ValueError:
            pass
    return DEFAULT
