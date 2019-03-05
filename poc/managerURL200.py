#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _    
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   < 
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
import sys
import requests

headers = {'user-agent': 'ceshi/0.0.1'}

def islive(ur,port):
    url='http://' + str(ur)+':'+str(port)+'/console/login/LoginForm.jsp'
    r = requests.get(url, headers=headers)
    return r.status_code

def run(url,port):
    if islive(url,port)==200:
        u='http://' + str(url)+':'+str(port)+'/console/login/LoginForm.jsp'
        print(u"[+]目标weblogic控制台地址暴露!\n[+]路径为:{}\n[+]请自行尝试弱口令爆破!".format(u))
    else:
        print(u"[-]目标weblogic控制台地址未找到!")

if __name__=="__main__":
    url = sys.argv[1]
    port = int(sys.argv[2])
    run(url,port)
    # run('127.0.0.1',7001)