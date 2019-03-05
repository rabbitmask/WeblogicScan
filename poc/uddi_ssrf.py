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
    url='http://' + str(ur)+':'+str(port)+'/uddiexplorer/'
    r = requests.get(url, headers=headers)
    # print(url,r.status_code)
    return r.status_code

def run(url,port):
    if islive(url,port)==200:
        print(u'[+]目标weblogic存在UDDI组件!\n[+]路径为:{}\n[+]请自行验证SSRF漏洞!'.format('http://' + str(url)+':'+str(port)+'/uddiexplorer/'))
    else:
        print(u"[-]目标weblogic UDDI组件默认路径不存在!")

if __name__=="__main__":
    url = sys.argv[1]
    port = int(sys.argv[2])
    run(url,port)