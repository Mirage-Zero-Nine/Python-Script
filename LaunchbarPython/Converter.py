#!/usr/bin/env python

#
# LaunchBar Action Script
#
__author__ = 'BorisMirage'
# --- coding:utf-8 ---
import sys

'''
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
        elif str(argument)[i] == 'e':
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

    def find_function(self):

        __temperature_measure = ['f', 'c', 'k']
        __length_measure = ['cm', 'inch', 'foot', 'feet', 'mile', 'm', 'yard', 'yd', 'km', 'mil']
        __weight_list = ['pound', 'oz', 'kg', 'lb', 'g']
        __volume_list = ['gallon', 'gal', 'ml', 'l']

        if self.scale in __temperature_measure:
            self.__temperature()
        elif self.scale in __length_measure:
            self.__length()
        elif self.scale in __weight_list:
            self.__weight()
        elif self.scale in __volume_list:
            self.__volume()
        else:
            print 'Wrong Scale!'

    def __temperature(self):

        if self.scale == 'f':
            Fahrenheit_to_Celsius = (self.number - 32) * 5 / 9
            Fahrenheit_to_Kelvin = Fahrenheit_to_Celsius + 273.15
            print self.number, 'F = ', Fahrenheit_to_Celsius, 'C'
            print self.number, 'F = ', Fahrenheit_to_Kelvin, 'K'
        elif self.scale == 'c':
            Celsius_to_Kelvin = self.number + 273.15
            Celsius_to_Fahrenheit = self.number * 9 / 5 + 32
            print self.number, 'C = ', Celsius_to_Fahrenheit, 'F'
            print self.number, 'C = ', Celsius_to_Kelvin, 'K'
        elif self.scale == 'k':
            Kelvin_to_Celsius = self.number - 273.15
            Kelvin_to_Fahrenheit = Kelvin_to_Celsius * 9 / 5 + 32
            print self.number, 'K = ', Kelvin_to_Celsius, 'C'
            print self.number, 'K = ', Kelvin_to_Fahrenheit, 'F'

    def __length(self):

        if self.scale == 'cm':
            cm_to_inch = self.number * 0.393701
            cm_to_feet = self.number * 0.0328084
            print self.number, 'cm = ', cm_to_inch, 'inch'
            print self.number, 'cm = ', cm_to_feet, 'feet'
        elif self.scale == 'inch':
            inch_to_cm = self.number * 2.54
            inch_to_meter = inch_to_cm / 100
            inch_to_feet = self.number / 12
            print self.number, 'cm = ', inch_to_cm, 'cm'
            print self.number, 'cm = ', inch_to_meter, 'meter'
            print self.number, 'cm = ', inch_to_feet, 'feet'
        elif self.scale == 'foot':
            foot_to_cm = self.number * 30.48
            foot_to_inch = self.number * 12
            foot_to_meter = foot_to_cm / 100
            foot_to_mile = self.number * 0.000189394
            if self.scale == 1:
                print self.number, 'foot = ', foot_to_cm, 'cm'
                print self.number, 'foot = ', foot_to_inch, 'inch'
                print self.number, 'foot = ', foot_to_meter, 'm'
                print self.number, 'foot = ', foot_to_mile, 'mile'
            else:
                print self.number, 'feet = ', foot_to_cm, 'cm'
                print self.number, 'feet = ', foot_to_inch, 'inch'
                print self.number, 'feet = ', foot_to_meter, 'm'
                print self.number, 'feet = ', foot_to_mile, 'mile'
        elif self.scale == 'mile' or self.scale == 'mil':
            mile_to_km = self.number * 1.60934
            print self.number, 'miles = ', mile_to_km, 'km'
        elif self.scale == 'm':
            m_to_mile = self.number * 0.000621371
            print self.number, 'm = ', m_to_mile, 'mile'
        elif self.scale == 'km':
            km_to_mile = self.number * 0.621371
            km_to_foot = self.number * 3280.84
            print self.number, 'km = ', km_to_mile, 'mile'
            print self.number, 'km = ', km_to_foot, 'foot'

    def __weight(self):

        if self.scale == 'pound' or self.scale == 'lb':
            pound_to_kg = self.number * 0.453592
            pound_to_ounces = self.number * 16
            print self.number, 'lb = ', pound_to_kg, 'kg'
            print self.number, 'lb = ', pound_to_ounces, 'oz'
        elif self.scale == 'ounce' or self.scale == 'oz':
            oz_to_g = self.number * 28.3495
            oz_to_pound = self.number / 16
            print self.number, 'oz = ', oz_to_g, 'g'
            print self.number, 'oz = ', oz_to_pound, 'lb'
        elif self.scale == 'g':
            g_to_oz = self.number * 0.035274
            g_to_lb = self.number * 0.00220462
            g_to_kg = self.number / 1000
            print self.number, 'g = ', g_to_oz, 'oz'
            print self.number, 'g = ', g_to_lb, 'lb'
            print self.number, 'g = ', g_to_kg, 'kg'

    def __volume(self):
        # __volume_list = ['gallon', 'gal', 'ml', 'l', 'oz']

        if self.scale == 'gal' or self.scale == 'gallon':
            gal_to_l = self.number * 3.78541
            print self.number, 'gal = ', gal_to_l, 'L'
        elif self.scale == 'ml':
            ml_to_gal = self.number * 0.000264172
            print self.number, 'ml = ', ml_to_gal, 'Gallon'


if __name__ == '__main__':
    list_para = parameter_fliter()
    Converter(list_para[0], list_para[1]).find_function()
