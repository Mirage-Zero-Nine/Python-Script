# --- coding:utf-8 ---
#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import re
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

items = []

item = {}
item['title'] = str(len(sys.argv) - 1) + ' arguments passed'
items.append(item)

# Note: The first argument is the script's path
for arg in sys.argv[1:]:
    item = {}
    item['title'] = 'Argument: ' + arg
    items.append(item)

# print (json.dumps(items))

def express():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30',
    }

    # Express id
    num = str(sys.argv[1])

    # Express request URL
    url = 'https://www.kuaidi100.com/autonumber/autoComNum?text='
    url = url + num

    # Set up session
    sessionExpress = requests.Session()
    sessionExpress.headers.update(headers)

    # Post
    sessionPost = sessionExpress.post(url)

    # Filter the result
    type = re.findall(r'(?<=comCode":")\w+', sessionPost.text)
    i = 0
    while True:
        getUrl = 'https://www.kuaidi100.com/query?type=' + str(type[i]) + '&postid=' + num
        i += 1
        getResult = sessionExpress.get(getUrl)
        checkMessage = '异常'
        if checkMessage in str(getResult.text):
            pass
        elif i > 10:
            break
        else:
            break
        
    # getUrl = 'https://www.kuaidi100.com/query?type=' + str(type[0]) + '&postid=' + num
    # getResult = sessionExpress.get(getUrl)
    # getResult.encoding = 'uft-8'

    # Format data and print it out
    getResult = getResult.json()
    i = 0
    while i < len(getResult['data']):
        '''
            {} One group of this means the para is an integer.
            "" One pair of this means the para is a string.
        '''
        time = getResult['data'][i]['time'].encode('utf-8')
        content = getResult['data'][i]['context'].encode('utf-8')
        print(time + content)
        i += 1

        # post https://www.kuaidi100.com/autonumber/autoComNum?text=
        # expressRespond = sessionExpress.get('https://www.kuaidi100.com/query?type=shunfeng&postid=').json()
        # expressRespond = json.dumps(expressRespond, ensure_ascii=False, indent=4)
        # print(expressRespond)

if __name__ == '__main__':
    express()
