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
from poc.index import *
from config.config_banners import banner



def pocbase(pocname,rip,rport):
    tmp,res=eval(pocname).run(rip,rport)
    return (tmp,res)

def poc(rip,rport):
    print ("[*] =========Task Start=========")
    for i in pocindex:
        tmp,res=pocbase(i,rip,rport)
        print(res)
    print ("[*] =========Task E n d=========")


def run():
    print(banner)
    print('Welcome To WeblogicScan !!!\nWhoami：https://github.com/rabbitmask')
    if len(sys.argv)<3:
        print('Usage: python3 WeblogicScan [IP] [PORT]')
    else:
        url = sys.argv[1]
        port = int(sys.argv[2])
        poc(url,port)

if __name__ == '__main__':
    run()

