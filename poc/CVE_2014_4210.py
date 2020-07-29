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


def islive(ur,port):
    url='http://' + str(ur)+':'+str(port)+'/uddiexplorer/'
    r = requests.get(url, headers=headers)
    return r.status_code

def run(url,port):
    if islive(url,port)==200:
        u='http://' + str(url)+':'+str(port)+'/uddiexplorer/'
        return (1,"[+] [{}] Weblogic UDDI module is exposed! The path is: {}".format(url+':'+str(port),u))
    else:
        return (0,"[-] [{}] Weblogic UDDI module default path does not exist!".format(url+':'+str(port)))

if __name__=="__main__":
    url = sys.argv[1]
    port = int(sys.argv[2])
    run(url,port)
