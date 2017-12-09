#!/usr/bin/env python

#stdlib
import math
import sys
# import custom libs
from utils import file_utils

class LocationCircle(object):
    '''
    The location of the transmitter can be defined as a locus of circle. ie, the transmitter can only be on
    the rim of a circle.
    '''
    def __init__(self, x_coord, y_coord, radius):
        self.x = x_coord
        self.y = y_coord
        self.r = radius

    def get_intersection_point(self, second_location_circle):
        '''
        By definition of the location of transmitter, it will always be at a certain point.
        Hence, the locus of the 2 circles will only meet at one point and one point only.
        :param second_location_circle:
        :return:
        '''

        self.loc_circle2 = second_location_circle
        #check here to ensure cirlces only touch at one point
        dist_between_centers = math.sqrt((self.loc_circle2.x - self.x)**2 + (self.loc_circle2.y - self.y)**2)
        # since only touching at one point, we can assume val a and b are the val of the radius
        if dist_between_centers == self.r + self.loc_circle2.r:
            x_intersect = self.x + self.r*(self.loc_circle2.x - self.x)/dist_between_centers
            y_intersect = self.y + self.r*(self.loc_circle2.y - self.y)/dist_between_centers
        else:
            print('Invalid data. Transmitter seems to be coming from 2 locations')

        return x_intersect, y_intersect


if __name__ == "__main__":
    list_of_circles = []
    input_data = file_utils.load_input_data(sys.argv[1])
    lines = input_data.readlines()
    input_data.close()

    for line in lines:
        list_of_circles.append(LocationCircle(float(line.strip().split()[0]),
                                              float(line.strip().split()[1]),
                                              float(line.strip().split()[2])))

    output = list_of_circles[0].get_intersection_point(list_of_circles[1])
    print(str(output[0]) + ' ' + str(output[1]))