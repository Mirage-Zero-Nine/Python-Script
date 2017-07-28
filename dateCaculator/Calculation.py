# -*- coding: utf-8 -*-
__author__ = 'BorisMirage'

from datetime import date
import datetime


class Choose(object):
    def __init__(self, select):
        self.select = select

    def raw(self):
        data_list = [0, 0, 1]
        if self.select == '1':
            raw_date = str(input('Import start date and gap days, use space to divide.\n'
                                 'e.g.: 2016.1.28 100\n')).split(' ', 1)
            data_list = [str(raw_date[0]).split('.', 2), str(raw_date[1]), int(self.select)]
        elif self.select == '2':
            raw_date = str(input('Import start date and end date, use space to divide.\n'
                                 'e.g.: 2016.1.28 2017.1.2\n')).split(' ', 1)
            data_list = [str(raw_date[0]).split('.', 2), str(raw_date[1]).split('.', 2), int(self.select)]
        elif self.select == '':
            data_list[2] = 0
        return data_list


class DateCalculator(object):
    def __init__(self, list_1, list_2, para):
        self.list_1 = list_1
        self.list_2 = list_2
        self.para = para

    def calculate(self):
        if self.para == 1:
            start = datetime.date(int(self.list_1[0]), int(self.list_1[1]), int(self.list_1[2]))
            result = start + datetime.timedelta(days=int(self.list_2))
            if int(self.list_2) > 0:
                print(self.list_2, 'days after', start, 'is:', result, '\n')
            elif int(self.list_2) < 0:
                print(abs(int(self.list_2)), 'days before', start, 'is:', result, '\n')
            else:
                print('Same date.\n')
        elif self.para == 2:
            start = datetime.date(int(self.list_1[0]), int(self.list_1[1]), int(self.list_1[2]))
            end = datetime.date(int(self.list_2[0]), int(self.list_2[1]), int(self.list_2[2]))
            result = str(end - start).split(' ', 1)
            print('From', start, 'to', end, '\nThere are', result[0], 'days. \n')
        elif self.para == 0:
            result = str(date.today() - datetime.date(2016, 1, 28)).split(' ', 1)
            print('We\'ve been together for', result[0], 'days.\n')


while True:
    num = input('Enter 1: Days ahead/after a date. \n'
                'Enter 2: Date calculate. \n')
    if num == '0':
        break
    else:
        try:
            raw_num = Choose(num).raw()
            DateCalculator(raw_num[0], raw_num[1], raw_num[2]).calculate()
        except:
            print('Wrong Number.\n')
exit()
