#!/usr/bin/env python

#stdlib
import sys
import textwrap



# import custom libs
from utils import file_utils

def text_justifier(text, width):
    for eachline in text:
        if len(eachline) > width:
            x = textwrap.wrap(eachline, width=width)
            for each in x:
                print(textwrap.fill(each, 20))


if __name__ == "__main__":
    input_text = file_utils.load_input_data(sys.argv[1])
    lines = input_text.readlines()
    input_text.close()
    width = int(lines[0].strip())

    del lines[0]
    lines = list(map(str.strip, lines))
    text_justifier(lines, width=width)




