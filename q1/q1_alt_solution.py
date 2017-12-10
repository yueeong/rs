#!/usr/bin/env python

#stdlib
import math
import sys
# import custom libs
from utils import file_utils


def get_intersection_point(x1, y1, r1, x0, y0, r0):
    '''
    Ratio of distance between the 2 points would apply to ratio of the x, y co-ord of the source.
    :param x1: x co-ord of second location
    :param y1: y co-ord of second location
    :param r1: r radius of second location
    :param x0:
    :param y0:
    :param r0:
    :return:
    '''
    ratio_dist_between_points = r0/(r0 + r1)
    # since one point is at origin, only need x1 and y1's co-ordinates.
    x3 = ratio_dist_between_points * x1
    y3 = ratio_dist_between_points * y1
    return x3, y3


if __name__ == "__main__":
    list_of_circles = []
    input_data = file_utils.load_input_data(sys.argv[1])
    lines = input_data.readlines()
    input_data.close()

    output = get_intersection_point(float(lines[0].strip().split()[0]),
                                    float(lines[0].strip().split()[1]),
                                    float(lines[0].strip().split()[2]),
                                    float(lines[1].strip().split()[0]),
                                    float(lines[1].strip().split()[1]),
                                    float(lines[1].strip().split()[2]))
    print(str(output[0]) + ' ' + str(output[1]))