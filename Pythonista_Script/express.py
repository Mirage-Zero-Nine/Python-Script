import clipboard # This is a specific module in Pythonista
import re
import requests

def express():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30',
    }  # Change headers!
    num = str(clipboard.get())
    url = 'https://www.kuaidi100.com/autonumber/autoComNum?text='
    url = url + num
    sessionExpress = requests.Session()
    sessionExpress.headers.update(headers)
    # sessionPost_1 = sessionExpress.post('https://www.kuaidi100.com/autonumber/autoComNum?text=')
    sessionPost = sessionExpress.post(url)
    type = re.findall(r'(?<=comCode":")\w+', sessionPost.text)
    i = 0
    while True:
        getUrl = 'https://www.kuaidi100.com/query?type=' + str(type[i]) + '&postid=' + num
        i += 1
        getResult = sessionExpress.get(getUrl)
        if '异常' not in str(getResult.text):
            break
    # getUrl = 'https://www.kuaidi100.com/query?type=' + str(type[0]) + '&postid=' + num
    # getResult = sessionExpress.get(getUrl)
    getResult.encoding = 'uft-8'
    getResult = getResult.json()
    i = 0
    while i < len(getResult['data']):
        '''
            {} One group of this means the para is an integer.
            "" One pair of this means the para is a string.
        '''
        print(getResult['data'][i]['time'], getResult['data'][i]['context'])
        i += 1
        # post https://www.kuaidi100.com/autonumber/autoComNum?text=
        # expressRespond = sessionExpress.get('https://www.kuaidi100.com/query?type=shunfeng&postid=').json()
        # expressRespond = json.dumps(expressRespond, ensure_ascii=False, indent=4)
        # print(expressRespond)

express()
