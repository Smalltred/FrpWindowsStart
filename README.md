# MinecraftFrpWindowsStart
---
在Windows上启动frp实现自动查找我的世界局域网端口的python程序

# 使用

1.安装相关的python库
```
pip install psutil
```
2.配置`frpc.ini`文件
```
[common]
server_addr = 服务器地址
server_port = 服务器通讯端口
token = 密钥

[mc]
type = tcp
local_ip = 127.0.0.1
local_port = 本地端口
remote_port = 要穿透远程端口
```
上面标记的按自己的填就好
不懂的去看frp的官方文档  

3.在客户端目录下创建```run.bat```文件填入以下内容
```
@echo off
title Frps内网穿透
:home
frpc -c frpc.ini
goto home
```  

3.把```main.py```也放入根目录即可，启动游戏进入存档打开对局域网开放，启动```main.py```即可，程序会自动获取端口并启动frp服务

# 说明
做这个东西的初衷就是图一个方便，联机的时候不用手动去`frp.ini`修改本地端口，而且自动获取端口修改`frp.ini`还是比较方便的.



#### 有什么bug可以提交[issues](https://github.com/Smalltred/MinecraftFrpWindowsStart/issues) 
