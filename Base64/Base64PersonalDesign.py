__author__ = 'BorisMirage'
# --- coding:utf-8 ---

import base64
import re

'''
text: the text that is to be encoded/decoded
flag: judge whether is to decode or encode, 1 = encode, 2 = decode
mode: choose which mode of encoding. 1 = normal, 2 = personal
'''


class Text(object):
    def __init__(self, text, flag, mode):
        self.sting_text = text
        self.int_flag = flag
        self.int_mode = mode

        if self.int_mode == 1:
            Text.normal_base64(self)
        else:
            Text.personalize_base64(self)

    def normal_base64(self):

        if self.int_flag == 1:
            self.sting_text = base64.b64encode(self.sting_text)
        elif self.int_flag == 0:
            self.sting_text = base64.b64decode(self.sting_text)

        return self.sting_text

    def personalize_base64(self):

        if self.int_flag == 1:

            self.sting_text = base64.b64encode(self.sting_text)

        elif self.int_flag == 0:

            if self.sting_text[len(self.sting_text) - 1] == '2':
                self.sting_text = self.sting_text[:len(self.sting_text) - 2] + '=='
            elif self.sting_text[len(self.sting_text) - 1] == '1':
                self.sting_text = self.sting_text[:len(self.sting_text) - 2] + '='
            elif self.sting_text[len(self.sting_text) - 1] == '0':
                self.sting_text = self.sting_text[:len(self.sting_text) - 2]

            self.sting_text = base64.b64decode(self.sting_text)

        find_equal_sign = re.findall(self.sting_text, '=')
        if find_equal_sign:
            self.sting_text = self.sting_text[:len(self.sting_text) - len(find_equal_sign)] + len(find_equal_sign)
        else:
            self.sting_text = self.sting_text + '0'

        return self.sting_text


if __name__ == '__main__':
    text = input('Put text here. \n')
    flag = input('Encode or decode? \n')
    mode = input('Which mode? \n')
    Text(text, flag, mode)
