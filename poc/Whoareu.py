#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import re
import socket
from time import sleep

def whoareu(rip,rport):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (rip, rport)
    sock.connect(server_address)
    sock.send(bytes.fromhex('74332031322e322e310a41533a3235350a484c3a31390a4d533a31303030303030300a0a'))
    sleep(1)
    v=(re.findall(r'HELO:(.*?).false', sock.recv(1024).decode()))[0]
    if v:
        return (1,"[+] [{}] Weblogic Version Is {}".format(rip+':'+str(rport),v))
    else:
        return (0,"[-] [{}] Weblogic Version Recognition Failed".format(rip+':'+str(rport)))

def run(rip,rport):
    return whoareu(rip,rport)