#!/usr/bin/env python


import sys
import itertools

# import custom libs
from utils import file_utils


def string_compactor(string_to_manipulate):
    string_to_manipulate = list(string_to_manipulate.replace(' ', ''))

    for each in range(len(string_to_manipulate)):
        try:
            if string_to_manipulate[each] == string_to_manipulate[each + 1]:
                del string_to_manipulate[each]
        except IndexError:
            break
    return ''.join(string_to_manipulate)


if __name__ == '__main__':
    instring = file_utils.load_input_data(sys.argv[1])
    lines = instring.read()
    instring.close()

    lines = string_compactor(lines)
    print(lines)
