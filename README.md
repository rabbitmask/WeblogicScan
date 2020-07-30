<div align=center><img src=WeblogicScan.jpg width="60%"></div>

# WeblogicScan
Weblogic一键漏洞检测工具，V1.5
```
软件作者：Tide_RabbitMask
免责声明：Pia!(ｏ ‵-′)ノ”(ノ﹏<。)
本工具仅用于安全测试，请勿用于非法使用，要乖哦~

V 1.5功能介绍：
提供一键poc检测，收录几乎全部weblogic历史漏洞。
详情如下：

    #控制台路径泄露
    Console  
    
    #SSRF：
    CVE-2014-4210      
    
    #JAVA反序列化
    CVE-2016-0638  
    CVE-2016-3510   
    CVE-2017-3248   
    CVE-2018-2628 
    CVE-2018-2893
    CVE-2019-2725
    CVE-2019-2729
    CVE_2019_2890
    
    #任意文件上传
    CVE-2018-2894   
    
    #XMLDecoder反序列化
    CVE-2017-3506
    CVE-2017-10271 
    
V 1.1 更新日志:
    删减全部EXP
    删减POC:CVE-2015-4852
    新增POC:CVE-2017-10271,CVE-2019-2725,CVE-2018-2894
    新增日志功能
    全新交互模式
    全新名称、Banner

V 1.2 更新日志:	
    新增离线依赖安装模式，满足内网测试需求：
    即新增文件夹:/whl/
    Usage：python3 install.py

V 1.3 更新日志:	
    全新支持Python3
    重写POC:CVE-2019-2725
    新增POC:CVE-2019-2729

V 1.4 更新日志:	[20200729]
    新增POC:CVE_2019_2890
    全新框架设计，高度封装与拟人化
    舍弃离线安装模块
    重点修复：从根本上解决脚本异常卡死问题（不同目标版本的异常通信造成）
    重点升级：从根本上解决脚本漏报误报问题（部分原因由py2->py3升级造成）
    # Not End：
    话说大家一直好奇其它同类型工具增加的CVE-2020-* 为什么一直没有在这里出现。
    其实相关的漏洞利用链以及最新的EXP我都有自己去复现或自己去写，手头也差不多是全的，
    但是如何把他们去靠谱的自动化集成一直是个问题，很多公开利用链是依赖ldap或没有回显可供正则的。
    :) 至于1.4高度封装与框架重新设计的目的，V1.5批量版本近期更新，敬请期待。

V 1.5 更新日志:	[20200730] [快不快？/嚣张脸:)]
    新增模块:Whoareu,基于T3的目标版本精确识别
    重点升级：增加批量扫描功能,智能兼容默认端口或自定义端口
    仅打印检测成功的内容，更多内容详见weblogic.log日志    
```
Software using Demo:	
===
```python WeblogicScan.py -h```
```
__        __   _     _             _        ____
\ \      / /__| |__ | | ___   __ _(_) ___  / ___|  ___ __ _ _ __
 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __| \___ \ / __/ _` | '_ \
  \ V  V /  __/ |_) | | (_) | (_| | | (__   ___) | (_| (_| | | | |
   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___| |____/ \___\__,_|_| |_|
                             |___/
                             By Tide_RabbitMask | V 1.5

Welcome To WeblogicScan !!!
Whoami：https://github.com/rabbitmask
usage: WeblogicScan.py [-h] [-u IP] [-p PORT] [-f FILE]

optional arguments:
  -h, --help  show this help message and exit

Scanner:
  -u IP       target ip
  -p PORT     target port
  -f FILE     target list
```
```python WeblogicScan.py -u 127.0.0.1 -p 7001```
```
__        __   _     _             _        ____
\ \      / /__| |__ | | ___   __ _(_) ___  / ___|  ___ __ _ _ __
 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __| \___ \ / __/ _` | '_ \
  \ V  V /  __/ |_) | | (_) | (_| | | (__   ___) | (_| (_| | | | |
   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___| |____/ \___\__,_|_| |_|
                             |___/
                             By Tide_RabbitMask | V 1.5

Welcome To WeblogicScan !!!
Whoami：https://github.com/rabbitmask
[*] =========Task Start=========
[+] [127.0.0.1:7001] Weblogic Version Is 10.3.6.0
[+] [127.0.0.1:7001] Weblogic console address is exposed! The path is: http://127.0.0.1:7001/console/login/LoginForm.jsp
[+] [127.0.0.1:7001] Weblogic UDDI module is exposed! The path is: http://127.0.0.1:7001/uddiexplorer/
[+] [127.0.0.1:7001] weblogic has a JAVA deserialization vulnerability:CVE-2016-0638
[-] [127.0.0.1:7001] weblogic not detected CVE-2016-3510
[-] [127.0.0.1:7001] weblogic not detected CVE-2017-10271
[-] [127.0.0.1:7001] weblogic not detected CVE-2017-3248
[-] [127.0.0.1:7001] weblogic not detected CVE-2017-3506
[+] [127.0.0.1:7001] weblogic has a JAVA deserialization vulnerability:CVE-2018-2628
[+] [127.0.0.1:7001] weblogic has a JAVA deserialization vulnerability:CVE-2018-2893
[-] [127.0.0.1:7001] weblogic not detected CVE-2018-2894
[-] [127.0.0.1:7001] weblogic not detected CVE-2019-2725
[-] [127.0.0.1:7001] weblogic not detected CVE-2019-2729
[+] [127.0.0.1:7001] weblogic has a JAVA deserialization vulnerability:CVE-2019-2890
[*] ==========Task End==========
```
```python WeblogicScan.py -f target.txt```
```
__        __   _     _             _        ____
\ \      / /__| |__ | | ___   __ _(_) ___  / ___|  ___ __ _ _ __
 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __| \___ \ / __/ _` | '_ \
  \ V  V /  __/ |_) | | (_) | (_| | | (__   ___) | (_| (_| | | | |
   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___| |____/ \___\__,_|_| |_|
                             |___/
                             By Tide_RabbitMask | V 1.5

Welcome To WeblogicScan !!!
Whoami：https://github.com/rabbitmask
[*] ========Task Num: [2]========
[*] =========Task Start=========
[+] [127.0.0.1:7001] Weblogic Version Is 10.3.6.0
[+] [172.19.19.19:7001] Weblogic Version Is 10.3.6.0
[+] [127.0.0.1:7001] Weblogic console address is exposed! The path is: http://127.0.0.1:7001/console/login/LoginForm.jsp
[+] [172.19.19.19:7001] Weblogic console address is exposed! The path is: http://172.19.19.19:7001/console/login/LoginForm.jsp
[+] [127.0.0.1:7001] Weblogic UDDI module is exposed! The path is: http://127.0.0.1:7001/uddiexplorer/
[+] [172.19.19.19:7001] Weblogic UDDI module is exposed! The path is: http://172.19.19.19:7001/uddiexplorer/
[+] [127.0.0.1:7001] weblogic has a JAVA deserialization vulnerability:CVE-2016-0638
[+] [172.19.19.19:7001] weblogic has a JAVA deserialization vulnerability:CVE-2016-0638
[+] [172.19.19.19:7001] weblogic has a JAVA deserialization vulnerability:CVE-2018-2628
[+] [127.0.0.1:7001] weblogic has a JAVA deserialization vulnerability:CVE-2018-2628
[+] [127.0.0.1:7001] weblogic has a JAVA deserialization vulnerability:CVE-2018-2893
[+] [172.19.19.19:7001] weblogic has a JAVA deserialization vulnerability:CVE-2018-2893
[+] [127.0.0.1:7001] weblogic has a JAVA deserialization vulnerability:CVE-2019-2890
[+] [172.19.19.19:7001] weblogic has a JAVA deserialization vulnerability:CVE-2019-2890
[*] ==========Task End==========
```
``` 
# Demo target.txt (端口默认为7001)

127.0.0.1:7001
192.168.1.1
192.168.1.1:80
```
``` 
# Demo Weblogic.log

2020-07-30 14:15:48,266 [+] [127.0.0.1:7001] Weblogic Version Is 10.3.6.0
2020-07-30 14:15:48,267 [+] [172.19.19.19:7001] Weblogic Version Is 10.3.6.0
2020-07-30 14:15:48,276 [+] [127.0.0.1:7001] Weblogic console address is exposed! The path is: http://127.0.0.1:7001/console/login/LoginForm.jsp
2020-07-30 14:15:48,314 [+] [172.19.19.19:7001] Weblogic console address is exposed! The path is: http://172.19.19.19:7001/console/login/LoginForm.jsp
2020-07-30 14:15:48,376 [+] [127.0.0.1:7001] Weblogic UDDI module is exposed! The path is: http://127.0.0.1:7001/uddiexplorer/
2020-07-30 14:15:48,393 [+] [172.19.19.19:7001] Weblogic UDDI module is exposed! The path is: http://172.19.19.19:7001/uddiexplorer/
2020-07-30 14:16:01,584 [+] [127.0.0.1:7001] weblogic has a JAVA deserialization vulnerability:CVE-2016-0638
2020-07-30 14:16:01,598 [+] [172.19.19.19:7001] weblogic has a JAVA deserialization vulnerability:CVE-2016-0638
2020-07-30 14:16:14,800 [-] [127.0.0.1:7001] weblogic not detected CVE-2016-3510
2020-07-30 14:16:14,802 [-] [172.19.19.19:7001] weblogic not detected CVE-2016-3510
2020-07-30 14:16:14,818 [-] [127.0.0.1:7001] weblogic not detected CVE-2017-10271
2020-07-30 14:16:14,821 [-] [172.19.19.19:7001] weblogic not detected CVE-2017-10271
2020-07-30 14:16:28,031 [-] [127.0.0.1:7001] weblogic not detected CVE-2017-3248
2020-07-30 14:16:28,035 [-] [172.19.19.19:7001] weblogic not detected CVE-2017-3248
2020-07-30 14:16:28,041 [-] [172.19.19.19:7001] weblogic not detected CVE-2017-3506
2020-07-30 14:16:28,048 [-] [127.0.0.1:7001] weblogic not detected CVE-2017-3506
2020-07-30 14:16:51,253 [+] [172.19.19.19:7001] weblogic has a JAVA deserialization vulnerability:CVE-2018-2628
2020-07-30 14:16:51,261 [+] [127.0.0.1:7001] weblogic has a JAVA deserialization vulnerability:CVE-2018-2628
2020-07-30 14:17:04,466 [+] [127.0.0.1:7001] weblogic has a JAVA deserialization vulnerability:CVE-2018-2893
2020-07-30 14:17:04,471 [-] [127.0.0.1:7001] weblogic not detected CVE-2018-2894
2020-07-30 14:17:04,609 [-] [127.0.0.1:7001] weblogic not detected CVE-2019-2725
2020-07-30 14:17:06,381 [+] [172.19.19.19:7001] weblogic has a JAVA deserialization vulnerability:CVE-2018-2893
2020-07-30 14:17:06,385 [-] [172.19.19.19:7001] weblogic not detected CVE-2018-2894
2020-07-30 14:17:06,553 [-] [172.19.19.19:7001] weblogic not detected CVE-2019-2725
2020-07-30 14:17:06,649 [-] [127.0.0.1:7001] weblogic not detected CVE-2019-2729
2020-07-30 14:17:08,591 [-] [172.19.19.19:7001] weblogic not detected CVE-2019-2729
2020-07-30 14:17:19,854 [+] [127.0.0.1:7001] weblogic has a JAVA deserialization vulnerability:CVE-2019-2890
2020-07-30 14:17:21,805 [+] [172.19.19.19:7001] weblogic has a JAVA deserialization vulnerability:CVE-2019-2890
```