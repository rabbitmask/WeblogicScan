<div align=center><img src=WeblogicScan.jpg width:45%></div>

# WeblogicScan
Weblogic vulnerability one-click poc detection.

	Software Author: Tide_RabbitMask.
	Thanks to the open source POC from the web.
	I have only carried out the magic transformation and interface unification.  
	Disclaimer：Pia!(ｏ ‵-′)ノ”(ノ﹏<。)
	This tool is for safety testing only,and should not be used for illegal use.
        
    V 1.1 Features：
    Provides a one-click poc detection that includes almost all weblogic history vulnerabilities.
    Details are as follows：
	
        #Console path leak
        Console  
        
        #SSRF：
        CVE-2014-4210      
        
        #JAVA deserialization
        CVE-2016-0638  
        CVE-2016-3510   
        CVE-2017-3248   
        CVE-2018-2628 
        CVE-2018-2893
        CVE-2019-2725		
        
        #Any file upload
        CVE-2018-2894   
        
        #XMLDecoder deserialization
        CVE-2017-10271 
        CVE-2017-3506
	
    V 1.1 Update log:
	
        Cut exp:all
        Cut poc:CVE-2015-4852
        New poc:CVE-2017-10271,CVE-2019-2725,CVE-2018-2894
        New Logging Function
        New Console
        New Name and Banner
	
		
Software using Demo:	
=========================================================================
	__        __   _     _             _        ____
	\ \      / /__| |__ | | ___   __ _(_) ___  / ___|  ___ __ _ _ __
	 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __| \___ \ / __/ _` | '_ \
	  \ V  V /  __/ |_) | | (_) | (_| | | (__   ___) | (_| (_| | | | |
	   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___| |____/ \___\__,_|_| |_|
				     |___/
						By Tide_RabbitMask | V 1.1

	Welcome To WeblogicScan !!
	[*]Console path test begins...
	[+]The target Weblogic console address is exposed!
	[+]The path is: http://127.0.0.1:7001/console/login/LoginForm.jsp
	[+]Please try weak password blasting!
	[*]CVE_2014_4210 test begins...
	[+]The target Weblogic UDDI module is exposed!
	[+]The path is: http://127.0.0.1:7001/uddiexplorer/
	[+]Please verify the SSRF vulnerability!
	[*]CVE_2016_0638 test begins...
	[+]The target weblogic has a JAVA deserialization vulnerability:CVE-2016-0638
	[*]CVE_2016_3510 test begins...
	[-]Target weblogic not detected CVE-2016-3510
	[*]CVE_2017_3248 test begins...
	[-]Target weblogic not detected CVE-2017-3248
	[*]CVE_2017_3506 test begins...
	[-]Target weblogic not detected CVE-2017-3506
	[*]CVE_2017_10271 test begins...
	[-]Target weblogic not detected CVE-2017-10271
	[*]CVE_2018_2628 test begins...
	[+]The target weblogic has a JAVA deserialization vulnerability:CVE-2018-2628
	[*]CVE_2018_2893 test begins...
	[+]The target weblogic has a JAVA deserialization vulnerability:CVE-2018-2893
	[*]CVE_2018_2894 test begins...
	[-]Target weblogic not detected CVE-2018-2894
	[*]CVE_2019_2725 test begins...
	[-]Target weblogic not detected CVE-2019-2725
	[*]The mission is over,the goal is 127.0.0.1:7001
