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

def currency():
    currencySession = requests.session()
    currencyRespond = currencySession.get('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote')

    root = ElementTree.fromstring(currencyRespond.content)
    node = root.findall('./resources/resource/field')
    print node[435].text

    '''
    result = float(node[434])*float(sys.argv[1])
    print '%.2f' % result
    
    
    i = 0
    while True:
        if node[i].text != 'USD/CNY':
            i +=1
        else:
            print i
            break


    
    for resource in root[1]:
        for name in resource:
            print type(name)
            print name.text
    if tag.text == 'USD/CNY':
        print root[1][0][i]
        break
    else:
        i += 1
    
    
    result = float(sys.argv[1])*currencyRespond
    print '%.2f' % currencyRespond
    
    '''


if __name__ == '__main__':
    currency()
