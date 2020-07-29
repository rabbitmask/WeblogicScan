#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import argparse
from poc.index import *



def pocbase(pocname,rip,rport):
    tmp,res=eval(pocname).run(rip,rport)
    return (tmp,res)

def poc(rip,rport):
    print ("[*] =========Task Start=========")
    for i in pocindex:
        tmp,res=pocbase(i,rip,rport)
        print(res)
    print ("[*] =========Task E n d=========")


def Weblogic_Console():
    parser = argparse.ArgumentParser()
    scanner = parser.add_argument_group('Scanner')

    scanner.add_argument("-u",dest='ip', help="target ip")
    scanner.add_argument("-p", dest='port', help="target port")

    args = parser.parse_args()

    if args.ip and args.port:
        poc(args.ip,int(args.port))

