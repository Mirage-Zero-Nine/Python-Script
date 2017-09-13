__author__ = 'BorisMirage'
# --- coding:utf-8 ---

import requests
import BeautifulSoup

'''
To Flit input phone number and to remove '+', '(', ')'.

'''


def NumberFliter(number):
    number = str(number)
    outputNumber = str()
    numberList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
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

def chaser(phoneNumber):
    url = 'https://npnr.org/202/344/7835/2023447835.html'
    # url = 'http://apilayer.net/api/validate?access_key=5d02acdb9792908ecfd0513095bbc43c&number=' + str(phoneNumber) + '&format=1'
    numberInfo = requests.get(url)
    newSoup = BeautifulSoup(numberInfo.text)
    print newSoup.find_all('td')


if __name__ == '__main__':
    rawNumber = raw_input('Number here.\n')
    chaser(NumberFliter(rawNumber))
