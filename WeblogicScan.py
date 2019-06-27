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
import poc.Console
import poc.CVE_2014_4210
import poc.CVE_2016_0638
import poc.CVE_2016_3510
import poc.CVE_2017_3248
import poc.CVE_2017_3506
import poc.CVE_2017_10271
import poc.CVE_2018_2628
import poc.CVE_2018_2893
import poc.CVE_2018_2894
import poc.CVE_2019_2725
import poc.CVE_2019_2729

version = "1.3"
banner='''
__        __   _     _             _        ____                  
\ \      / /__| |__ | | ___   __ _(_) ___  / ___|  ___ __ _ _ __  
 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __| \___ \ / __/ _` | '_ \ 
  \ V  V /  __/ |_) | | (_) | (_| | | (__   ___) | (_| (_| | | | |
   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___| |____/ \___\__,_|_| |_|
                             |___/ 
                             By Tide_RabbitMask | V {} 
'''.format(version)

def PocS(rip,rport):
    print('[*]Console path is testing...')
    try:
        poc.Console.run(rip, rport)
    except:
        print ("[-]Target Weblogic console address not found.")

    print('[*]CVE_2014_4210 is testing...')
    try:
        poc.CVE_2014_4210.run(rip, rport)
    except:
        print ("[-]CVE_2014_4210 not detected.")

    print('[*]CVE_2016_0638 is testing...')
    try:
        poc.CVE_2016_0638.run(rip, rport, 0)
    except:
        print ("[-]CVE_2016_0638 not detected.")

    print('[*]CVE_2016_3510 is testing...')
    try:
        poc.CVE_2016_3510.run(rip, rport, 0)
    except:
        print ("[-]CVE_2016_3510 not detected.")

    print('[*]CVE_2017_3248 is testing...')
    try:
        poc.CVE_2017_3248.run(rip, rport, 0)
    except:
        print ("[-]CVE_2017_3248 not detected.")

    print('[*]CVE_2017_3506 is testing...')
    try:
        poc.CVE_2017_3506.run(rip, rport, 0)
    except:
        print ("[-]CVE_2017_3506 not detected.")

    print('[*]CVE_2017_10271 is testing...')
    try:
        poc.CVE_2017_10271.run(rip, rport, 0)
    except:
        print("[-]CVE_2017_10271 not detected.")

    print('[*]CVE_2018_2628 is testing...')
    try:
        poc.CVE_2018_2628.run(rip, rport, 0)
    except:
        print("[-]CVE_2018_2628 not detected.")

    print('[*]CVE_2018_2893 is testing...')
    try:
        poc.CVE_2018_2893.run(rip, rport, 0)
    except:
        print("[-]CVE_2018_2893 not detected.")

    print('[*]CVE_2018_2894 is testing...')
    try:
        poc.CVE_2018_2894.run(rip, rport, 0)
    except:
        print("[-]CVE_2018_2894 not detected.")

    print('[*]CVE_2019_2725 is testing...')
    try:
        poc.CVE_2019_2725.run(rip, rport, 0)
    except:
        print("[-]CVE_2019_2725 not detected.")

    print('[*]CVE_2019_2729 is testing...')
    try:
        poc.CVE_2019_2729.run(rip, rport, 0)
    except:
        print("[-]CVE_2019_2729 not detected.")

    print ("[*]Happy End,the goal is {}:{}".format(rip,rport))

def run():
    print(banner)
    print('Welcome To WeblogicScan !!!\nWhoami：rabbitmask.github.io')
    if len(sys.argv)<3:
        print('Usage: python3 WeblogicScan [IP] [PORT]')
    else:
        url = sys.argv[1]
        port = int(sys.argv[2])
        PocS(url,port)

if __name__ == '__main__':
    run()

