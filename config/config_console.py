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

from config.config_logging import loglog
from multiprocessing import Pool, Manager
from poc.index import *

def pocbase(pocname,rip,rport):
    tmp,res=eval(pocname).run(rip,rport)
    return (tmp,res)

def poc(rip,rport):
    print ("[*] =========Task Start=========")
    for i in pocindex:
        tmp,res=pocbase(i,rip,rport)
        loglog(res)
        print(res)
    print ("[*] =========Task E n d=========")

def pocs(rip,rport,q):
    for i in pocindex:
        tmp,res=pocbase(i,rip,rport)
        loglog(res)
        if tmp==1:
            print(res)
    q.put(rip,rport)


def poolmana(filename):
    fr=open(filename,'r')
    url=fr.readlines()
    fr.close()
    print ("[*] ========Task Num: [{}]========".format(len(url)))
    print ("[*] =========Task Start=========")
    p = Pool(10)
    q = Manager().Queue()
    for i in url:
        i=i.replace('\n','')
        if ':' in i:
            ip=i.split(':')[0]
            port=int(i.split(':')[1])
            p.apply_async(pocs, args=(ip,port,q,))
        else:
            ip=i
            port=7001
            p.apply_async(pocs, args=(ip,port,q,))
    p.close()
    p.join()
    print ("[*] ==========Task End==========")


def Weblogic_Console():
    parser = argparse.ArgumentParser()
    scanner = parser.add_argument_group('Scanner')

    scanner.add_argument("-u",dest='ip', help="target ip")
    scanner.add_argument("-p", dest='port', help="target port")
    scanner.add_argument("-f", dest='file', help="target list")

    args = parser.parse_args()

    if args.ip and args.port:
        poc(args.ip,int(args.port))
    elif args.file:
        poolmana(args.file)

