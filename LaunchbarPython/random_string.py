__author__ = 'BorisMirage'
# --- coding:utf-8 ---
#!/usr/bin/env python
#
# LaunchBar Action Script
#
import sys
import json
import time
import hashlib
import subprocess
import random
from passlib.hash import sha512_crypt


class random_string(object):
    def __init__(self, base_string):
        self.string = base_string

    def generate_random(self):

        # Hash string
        hash_string = hashlib.sha224(self.string).hexdigest()

        # Expand string to contain 26 letters, rather than in hash 16.
        code = sha512_crypt.encrypt(hash_string, rounds=5000, salt=str(random.randint(0, 100)))
        code = code[12:21]

        # Copy to clipboard
        process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
        process.communicate(code.encode('utf-8'))
        print code

if __name__ == '__main__':
    random_string(str(time.localtime())).generate_random()

