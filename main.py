#!/usr/bin/python
# -- coding: utf-8 --
import psutil
import os
from configobj import ConfigObj


# 获取pid
def find_pid(process):
    for i in psutil.process_iter():
        if i.name() == process_name:
            return i.pid
    else:
        print("未找到")


# 查网络信息 端口号
def find_port(process_pid):
    network_info = psutil.net_connections()
    for i in network_info:
        if i.pid == process_pid:
            if i.laddr[0] == "0.0.0.0" and i.status == "LISTEN":
                print(f"获取成功，游戏内端口: {i.laddr[1]}")
                return i.laddr[1]
        else:
            pass


def setting(port):
    local_port = port
    config['mc']['local_port'] = local_port
    print("已使用此端口")
    config.write()


def run_frp():
    print("启动成功！")
    os.system("Run.bat")


if __name__ == '__main__':
    config = ConfigObj('frpc.ini', encoding='UTF-8')
    process_name = 'java.exe'
    pid = find_pid(process_name)
    game_port = find_port(pid)
    setting(game_port)
    run_frp()

