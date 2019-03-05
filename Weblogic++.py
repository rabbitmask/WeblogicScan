#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
import poc.managerURL200
import poc.uddi_ssrf
import poc.CVE_2015_4852
import poc.CVE_2016_0638
import poc.CVE_2016_3510
import poc.CVE_2017_3248
import poc.CVE_2017_3506
import poc.CVE_2018_2628
import poc.CVE_2018_2893


version = "1.0"
banner='''
__        __   _     _             _                    
\ \      / /__| |__ | | ___   __ _(_) ___     _     _   
 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __|  _| |_ _| |_ 
  \ V  V /  __/ |_) | | (_) | (_| | | (__  |_   _ _   _|
   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___|   |_|   |_|  
                             |___/    
                             
                             By Tide_RabbitMask | V {} 
'''.format(version)
print (banner)
print ('Welcome To Weblogic++ !!')
about=u'''
=======================================================
    软件作者：Tide_RabbitMask
    免责声明：Pia!(ｏ ‵-′)ノ”(ノ﹏<。)
    本工具仅用于安全测试，请勿用于非法使用，要乖哦~
        
    V 1.0功能介绍：
    提供一键poc检测，收录几乎全部weblogic历史漏洞。
    详情如下：
        #控制台路径泄露
        managerURL200  
        
        #SSRF：
        uddi-ssrf       
        
        #JAVA反序列化：
        CVE-2015-4852  
        CVE-2016-0638  
        CVE-2016-3510   
        CVE-2017-3248   
        CVE-2018-2628 
        CVE-2018-2893   
        
        #任意文件上传
        CVE-2018-2894   
        
        #XMLDecoder反序列化：
        CVE-2017-10271 
        CVE-2017-3506
    
    V1.*功能预告：
        多进程并发
        修复建议
        模块优化
        交互优化 
        报告生成
=======================================================
        
'''
menu=u'''
    1、开启POC检测
    2、开启EXP利用
    3、关于本软件
'''
def board():
    while True:
        print (menu)
        a=input()
        if a == exit:
            break
        if a == 1:
            rip = raw_input("Please enter the IP:")
            if rip=="exit":
                break
            rport = input("Please enter the port:")
            if rport=="exit":
                break
            work(rip,rport)
        if a == 2:
            print(u'exp的使用方式各异且功能强大，所以笔者在此统一整理，诸君根据poc检测结果人工补测，详见exp目录。')
        if a == 3:
            print (about)
        else:
            pass

def work(rip,rport):
    print(u'[*]开始控制台路径检测')
    try:
        poc.managerURL200.run(rip, rport)
    except:
        print (u"控制台路径检测异常，请手动补测")
    print(u'[*]开始SSRF检测')
    try:
        poc.uddi_ssrf.run(rip,rport)
    except:
        print (u"SSRF检测异常，请手动补测")
    print(u'[*]开始CVE_2015_4852检测')
    try:
        poc.CVE_2015_4852.run(rip,rport)
    except:
        print (u"CVE_2015_4852检测异常，请手动补测")
    print(u'[*]开始CVE_2016_0638检测')
    try:
        poc.CVE_2016_0638.run(rip,rport,0)
    except:
        print (u"CVE_2016_0638检测异常，请手动补测")
    print(u'[*]开始CVE_2016_3510检测')
    try:
        poc.CVE_2016_3510.run(rip, rport, 0)
    except:
        print (u"CVE_2016_3510检测异常，请手动补测")
    print(u'[*]开始CVE_2017_3248检测')
    try:
        poc.CVE_2017_3248.run(rip, rport, 0)
    except:
        print (u"CVE_2017_3248检测异常，请手动补测")
    print(u'[*]开始CVE_2017_3506检测')
    try:
        poc.CVE_2017_3506.run(rip, rport)
    except:
        print (u"CVE_2017_3506检测异常，请手动补测")
    print(u'[*]开始CVE_2018_2628检测')
    try:
        poc.CVE_2018_2628.run(rip, rport, 0)
    except:
        print (u"CVE_2018_2628检测异常，请手动补测")
    print(u'[*]开始CVE_2018_2893检测')
    try:
        poc.CVE_2018_2893.run(rip, rport, 0)
    except:
        print (u"CVE_2018_2893检测异常，请手动补测")
    print (u"[*]本次检测任务结束，目标 {}:{}").format(rip,rport)

def run():
    board()

if __name__ == '__main__':
    run()
