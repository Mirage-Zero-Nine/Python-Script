#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
from xml.etree import ElementTree

items = []

item = {}
item['title'] = str(len(sys.argv) - 1) + ' arguments passed'
items.append(item)

# Note: The first argument is the script's path
for arg in sys.argv[1:]:
    item = {}
    item['title'] = 'Argument: ' + arg
    items.append(item)

# print json.dumps(items) This line should be ignored in order to avoid unnecessary output

import requests


def NumberFliter(number):
    number = str(number)
    outputNumber = str()
    numberList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
    i = 0
    while i < len(number):
        if number[i] in numberList:
            outputNumber = outputNumber + number[i]
        '''
        elif number[i] == '+':
            i += 1
        '''
        i += 1

    return outputNumber

def currency():
    currencySession = requests.session()
    currencyRespond = currencySession.get('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote')
    root = ElementTree.fromstring(currencyRespond.content)
    node = root.findall('./resources/resource/field') # This line is to find current rate for USD/CNY. Any other rate can be found on this website
    if str(node[434].text) != 'USD/CNY':
        print 'Error!'
    else:
        result = float(node[435].text)*float(NumberFliter(sys.argv[1]))
        print '%.2f' % result


if __name__ == '__main__':
    currency()
