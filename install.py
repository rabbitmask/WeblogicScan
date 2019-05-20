#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
import os

def run():
    os.system("pip install whl/certifi-2019.3.9-py2.py3-none-any.whl")
    os.system("pip install whl/chardet-3.0.4-py2.py3-none-any.whl")
    os.system("pip install whl/idna-2.8-py2.py3-none-any.whl")
    os.system("pip install whl/urllib3-1.25.2-py2.py3-none-any.whl")
    os.system("pip install whl/requests-2.22.0-py2.py3-none-any.whl")
    print ("install success!")

if __name__ == '__main__':
    run()
