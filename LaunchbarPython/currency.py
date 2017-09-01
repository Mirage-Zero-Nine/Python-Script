#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys

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
    currencyRespond = currencySession.get('http://apilayer.net/api/live?access_key=8f98bbab6dc62d96b2846c5a9e8e592b').json()['quotes']['USDCNY']
    result = float(sys.argv[1])*currencyRespond
    print result

if __name__ == '__main__':
    currency()
