__author__ = 'BorisMirage'
# --- coding:utf-8 ---

import re
import requests

'''
Work on both Python 2 and Python 3

**Need to import your cookie from browser.**
'''


def v2ex():
    redo_header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38',
        'Referer': 'https://www.v2ex.com/signin',
        'Origin': 'https://www.v2ex.com'}
    redo_header['cookie'] = 'Your cookie here'

    session = requests.Session()
    session.headers = redo_header
    resp = session.get('https://www.v2ex.com/mission/daily')

    if u'每日登录奖励已领取' in resp.text:
        print('Already got it.')
    else:
        resp = session.get('http://www.v2ex.com' + re.search(r'/mission/daily/redeem\?once=\d+', resp.text).group())
        print(resp.ok)


if __name__ == '__main__':
    v2ex()
