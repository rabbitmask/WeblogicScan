#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\

'''
from config.config_banners import banner
from config.config_console import Weblogic_Console


def run():
    print(banner)
    print('Welcome To WeblogicScan !!!\nWhoami：https://github.com/rabbitmask')
    Weblogic_Console()

if __name__ == '__main__':
    run()
