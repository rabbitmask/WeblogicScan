<div align=center><img src=WeblogicScan.jpg width="60%"></div>

# WeblogicScan
Weblogic一键检测工具，V1.3

	软件作者：Tide_RabbitMask
	免责声明：Pia!(ｏ ‵-′)ノ”(ノ﹏<。)
	本工具仅用于安全测试，请勿用于非法使用，要乖哦~
	
	V 1.3功能介绍：
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

Software using Demo:	
===
	__        __   _     _             _        ____
	\ \      / /__| |__ | | ___   __ _(_) ___  / ___|  ___ __ _ _ __
	 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __| \___ \ / __/ _` | '_ \
	  \ V  V /  __/ |_) | | (_) | (_| | | (__   ___) | (_| (_| | | | |
	   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___| |____/ \___\__,_|_| |_|
				     |___/
				     By Tide_RabbitMask | V 1.3

	Welcome To WeblogicScan !!!
	Whoami：rabbitmask.github.io
	Usage: python WeblogicScan [IP] [PORT]
	[*]Console path is testing...
	[+]The target Weblogic console address is exposed!
	[+]The path is: http://127.0.0.1:7001/console/login/LoginForm.jsp
	[+]Please try weak password blasting!
	[*]CVE_2014_4210 is testing...
	[+]The target Weblogic UDDI module is exposed!
	[+]The path is: http://127.0.0.1:7001/uddiexplorer/
	[+]Please verify the SSRF vulnerability!
	[*]CVE_2016_0638 is testing...
	[-]Target weblogic not detected CVE-2016-0638
	[*]CVE_2016_3510 is testing...
	[-]Target weblogic not detected CVE-2016-3510
	[*]CVE_2017_3248 is testing...
	[-]Target weblogic not detected CVE-2017-3248
	[*]CVE_2017_3506 is testing...
	[-]Target weblogic not detected CVE-2017-3506
	[*]CVE_2017_10271 is testing...
	[-]Target weblogic not detected CVE-2017-10271
	[*]CVE_2018_2628 is testing...
	[-]Target weblogic not detected CVE-2018-2628
	[*]CVE_2018_2893 is testing...
	[-]Target weblogic not detected CVE-2018-2893
	[*]CVE_2018_2894 is testing...
	[-]Target weblogic not detected CVE-2018-2894
	[*]CVE_2019_2725 is testing...
	[+]The target weblogic has a JAVA deserialization vulnerability:CVE-2019-2725
	[+]Your current permission is:  rabbitmask\rabbitmask
	[*]CVE_2019_2729 is testing...
	[+]The target weblogic has a JAVA deserialization vulnerability:CVE-2019-2729
	[+]Your current permission is:  rabbitmask\rabbitmask
	[*]Happy End,the goal is 127.0.0.1:7001	

