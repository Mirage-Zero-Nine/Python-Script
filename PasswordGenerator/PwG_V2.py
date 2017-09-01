__author__ = 'BorisMirage'
# --- coding:utf-8 ---
import time
import hashlib
import subprocess
import os
from passlib.hash import sha512_crypt


class Pw(object):
    def __init__(self, source, code, record=0):
        self.record = record  # Decide whether save password or not
        self.source = source  # Import via user
        self.code = code  # Import via user

    def encrypt(self):
        cache = ''
        salt = hashlib.md5((self.source + self.code).encode('utf-8')).hexdigest()[0:16]
        code = sha512_crypt.encrypt(hashlib.md5(self.source.encode('utf-8')).hexdigest(), rounds=5000, salt=salt)[::-1]
        length_code = len(code) - 1
        while length_code > 0:
            temp = code[length_code]
            if temp.isalnum():
                cache += str(temp)
            length_code -= 1
        code = cache[-3:] + '-' + cache[-6:-3] + '-' + cache[-9:-6] + '-' + cache[-12:-9]
        return code

    def write_to_clipboard(self, string):
        if os.name == 'posix':
            process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
            process.communicate(string.encode('utf-8'))
        elif os.name == 'nt':
            command = 'echo' + string.strip() + '| clip'
            os.system(command)

    def save_pw(self, final_code):
        Pw(final_code, final_code).write_to_clipboard(final_code)
        current = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # Get current time
        os.chdir(os.path.abspath('.'))  # This is the current path. You can move to wherever you like.
        try:
            f = open('Storage.txt', 'r')  # Open file r = read
            text = f.read()  # Check whether file is vacant
        except FileNotFoundError:
            f = open('Storage.txt', 'a')  # a = append
            text = f.read()  # Check whether file is vacant
        content = ['Information : ', self.source, '\n', 'Password : ', final_code, '\n', 'Time : ', current, '\n']
        content = ''.join(content)
        if self.record == 1:
            if text != '':
                content = ['\n', content]
                content = ''.join(content)
            f.write(content)
        return content


def main():
    while True:
        info = str(input('information,code,save\n'
                         'save=0: do not save password. save=1: save password.\n'))
        if info == '0':
            break
        else:
            try:
                list_0 = info.split(',', 2)
                pw_object = Pw(list_0[0], list_0[1], int(list_0[2]))
            except IndexError:
                list_1 = info.split(',', 1)
                pw_object = Pw(list_1[0], list_1[1])
            pw = pw_object.encrypt()
        print(pw_object.save_pw(pw))
    exit()


if __name__ == '__main__':
    main()
