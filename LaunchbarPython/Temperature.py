#!/usr/bin/env python

#
# LaunchBar Action Script
#
__author__ = 'BorisMirage'
# --- coding:utf-8 ---
import sys

'''
items = []

item = {}
item['title'] = str(len(sys.argv) - 1) + ' arguments passed'
items.append(item)



# Note: The first argument is the script's path
for arg in sys.argv[1:]:
    item = {}
    item['title'] = 'Argument: ' + arg
    items.append(item)

print json.dumps(items)


[F] = [C] * 9/5 + 32
[C] = ([F] - 32) * 5/9
[K] = [C] + 273.15
[C] = [K] - 273.15

'''


def parameter_fliter():
    i = 0
    string_input = ''
    string_scale = 'c'
    while i < len(str(sys.argv[1])):
        if str(sys.argv[1])[i].isdigit():
            string_input = string_input + str(sys.argv[1])[i]
        elif str(sys.argv[1])[i].isalpha():
            string_scale = str(sys.argv[1])[i]
        elif str(sys.argv[1])[i] == '.':
            string_input = string_input + str(sys.argv[1])[i]
        i += 1
    result_list = [float(string_input), string_scale]
    return result_list


class Temperature(object):
    def __init__(self, float_number, scale):
        self.number = float(float_number)
        self.scale = scale

    def convert(self):
        if self.scale == 'f' or self.scale == 'F':
            int_Fahrenheit_to_Celsius = (self.number - 32) * 5 / 9
            int_Fahrenheit_to_Kelvin = int_Fahrenheit_to_Celsius + 273.15
            print self.number, 'F = ', int_Fahrenheit_to_Celsius, 'C'
            print self.number, 'F = ', int_Fahrenheit_to_Kelvin, 'K'
        elif self.scale == 'c' or self.scale == 'C':
            int_Celsius_to_Kelvin = self.number + 273.15
            int_Celsius_to_Fahrenheit = self.number * 9 / 5 + 32
            print self.number, 'C = ', int_Celsius_to_Fahrenheit, 'F'
            print self.number, 'C = ', int_Celsius_to_Kelvin, 'K'
        elif self.scale == 'k' or self.scale == 'K':
            int_Kelvin_to_Celsius = self.number - 273.15
            int_Kelvin_to_Fahrenheit = int_Kelvin_to_Celsius * 9 / 5 + 32
            print self.number, 'K = ', int_Kelvin_to_Celsius, 'C'
            print self.number, 'K = ', int_Kelvin_to_Fahrenheit, 'F'
        else:
            print 'Wrong Scale!'


if __name__ == '__main__':
    list_para = parameter_fliter()
    Temperature(list_para[0], list_para[1]).convert()
