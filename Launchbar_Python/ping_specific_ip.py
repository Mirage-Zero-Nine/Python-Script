__author__ = 'BorisMirage'
# --- coding:utf-8 ---
import subprocess
import re

# Input target ip here
ip_list = '''192.168.1.1
192.168.1.1
'''

ip_list = ip_list.split('\n')


def ping():
    for i in range(len(ip_list) - 1):
        ip = ip_list[int(i)]
        command = 'ping ' + str(ip) + ' -c 10'
        sub = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out = sub.communicate()[0]
        time = re.findall('\d+\.?\d+?\/\d+\.?\d+?\/\d+\.?\d+?', str(out))
        time_list = str(time[0]).split('/')
        print('ping IP:', ip)
        print('Min:', time_list[0])
        print('Ave:', time_list[1])
        print('Max:', time_list[2])

        
if __name__ == '__main__':
    ping()
