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
    string_scale = ''
    argument = str(sys.argv[1])
    while i < len(str(argument)):
        if str(argument)[i].isdigit():
            string_input = string_input + str(argument)[i]
        elif str(argument)[i].isalpha():
            string_scale = string_scale + str(argument)[i]
        elif str(sys.argv[1])[i] == '.':
            string_input = string_input + str(argument)[i]
        i += 1
    result_list = [float(string_input), string_scale]
    return result_list


class Converter(object):
    def __init__(self, float_number, scale):
        self.number = float(float_number)
        self.scale = str(scale).lower()

    def converter_function(self):
        if self.scale == 'f':
            float_Fahrenheit_to_Celsius = (self.number - 32) * 5 / 9
            float_Fahrenheit_to_Kelvin = float_Fahrenheit_to_Celsius + 273.15
            print self.number, 'F = ', float_Fahrenheit_to_Celsius, 'C'
            print self.number, 'F = ', float_Fahrenheit_to_Kelvin, 'K'
        elif self.scale == 'c':
            float_Celsius_to_Kelvin = self.number + 273.15
            float_Celsius_to_Fahrenheit = self.number * 9 / 5 + 32
            print self.number, 'C = ', float_Celsius_to_Fahrenheit, 'F'
            print self.number, 'C = ', float_Celsius_to_Kelvin, 'K'
        elif self.scale == 'k':
            float_Kelvin_to_Celsius = self.number - 273.15
            float_Kelvin_to_Fahrenheit = float_Kelvin_to_Celsius * 9 / 5 + 32
            print self.number, 'K = ', float_Kelvin_to_Celsius, 'C'
            print self.number, 'K = ', float_Kelvin_to_Fahrenheit, 'F'
        elif self.scale == 'cm':
            float_cm_to_inch = self.number * 0.393701
            float_cm_to_feet = self.number * 0.0328084
            print self.number, 'cm = ', float_cm_to_inch, 'inch'
            print self.number, 'cm = ', float_cm_to_feet, 'feet'
        elif self.scale == 'inch':
            float_inch_to_cm = self.number * 2.54
            float_inch_to_meter = float_inch_to_cm / 100
            float_inch_to_feet = self.number / 12
            print self.number, 'cm = ', float_inch_to_cm, 'cm'
            print self.number, 'cm = ', float_inch_to_meter, 'meter'
            print self.number, 'cm = ', float_inch_to_feet, 'feet'

        else:
            print 'Wrong Scale!'


if __name__ == '__main__':
    list_para = parameter_fliter()
    Converter(list_para[0], list_para[1]).converter_function()
