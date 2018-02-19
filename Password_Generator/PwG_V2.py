__author__ = 'BorisMirage'
# --- coding:utf-8 ---
import hashlib
import subprocess
import os
from passlib.hash import sha512_crypt


class Password(object):
    def __init__(self, string='17-12-09'):
        self.string = string

    def __choose_method(self):
        method = str(input('Info input here. \n'))
        return method

    def __encrypt(self):
        new_info = self.__choose_method()
        cache = ''
        salt = hashlib.md5(new_info.encode('utf-8')).hexdigest()[0:16]
        code = sha512_crypt.encrypt(hashlib.md5(new_info.encode('utf-8')).hexdigest(), rounds=5000, salt=salt)[::-1]
        length_code = len(code) - 1
        while length_code > 0:
            temp = code[length_code]
            if temp.isalnum():
                cache += str(temp)
            length_code -= 1
        code = cache[-3:] + '-' + cache[-6:-3] + '-' + cache[-9:-6] + '-' + cache[-12:-9]
        if os.name == 'posix':
            process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
            process.communicate(code.encode('utf-8'))
        elif os.name == 'nt':
            command = 'echo' + code.strip() + '| clip'
            os.system(command)
        return code

    # def __write_to_clipboard(self, string):
    #     if os.name == 'posix':
    #         process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    #         process.communicate(string.encode('utf-8'))
    #     elif os.name == 'nt':
    #         command = 'echo' + string.strip() + '| clip'
    #         os.system(command)

    def generate(self):
        self.__encrypt()


if __name__ == '__main__':
    Password().generate()
