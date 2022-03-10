#!/usr/bin/python
# -- coding: utf-8 --
# @Author : Small_tred 
# @Time : 2022/3/10 20:17
import os
import sys
import psutil
from configobj import ConfigObj


# 获取pid  没有获取到pid就返回 none
def findPid():
    for i in psutil.process_iter():
        if i.name() == process_name:
            print(f"获取成功,进程PID: {i.pid}")
            return i.pid
    input("请检查是否启动了游戏或者打开了对局域网开放，按任意键关闭。\n")
    sys.exit()


# 根据pid查端口 做none判断 没有端口则不做修改 并关闭程序
def findPort():
    network_info = psutil.net_connections()
    for i in network_info:
        if i.pid == pid:
            if i.laddr[0] == "0.0.0.0" and i.status == "LISTEN":
                print(f"获取成功，游戏内端口: {i.laddr[1]}")
                return i.laddr[1]


# 写入端口到配置文件
def saveConfig():
    if os.path.exists(runfile):
        config['mc']['local_port'] = port
        config.write()
    else:
        with open(runfile, "w", encoding="UTF-8") as f:
            f.write(runconfig)


# 启动frp
def runFrp():
    os.system("Run.bat")


if __name__ == '__main__':
    runconfig = """@echo off
title Frp内网穿透
:home
frpc -c frpc.ini
goto home
"""
    config = ConfigObj('frpc.ini', encoding='UTF-8')
    runfile = "Run.bat"
    process_name = 'java.exe'
    pid = findPid()
    port = findPort()
    saveConfig()
    runFrp()
