#!/usr/bin/env python3
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
from config.config_requests import headers

VUL=['CVE-2018-2894']


def islive(ur,port):
    url='http://' + str(ur)+':'+str(port)+'/ws_utc/resources/setting/options/general'
    r = requests.get(url, headers=headers)
    return r.status_code

def run(rip,rport):
    if islive(rip,rport)!=404:
        return (1, '[+] [{}] weblogic has a JAVA deserialization vulnerability:{}'.format(rip + ':' + str(rport), VUL[0]))
    else:
        return (0, '[-] [{}] weblogic not detected {}'.format(rip + ':' + str(rport), VUL[0]))

if __name__=="__main__":
    url = sys.argv[1]
    port = int(sys.argv[2])
    run(url,port)
