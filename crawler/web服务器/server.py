#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

s = socket.socket()

#本机主机名
#host = socket.gethostname()
host = '172.24.133.33'
#端口号
port = 8080

'''
监听某个特定的地址
'''
#连接客户端
s.bind((host, port))
#最多等待次数
s.listen(5)

while True:
    #接受客户端的连接,c 为客户端套接字，addr 为客户端的地址
    c, addr = s.accept()
    print 'c=', c, 'addr=', addr
    print 'get connection from', addr
    #传输数据
    c.send('thank for you connection')
    c.close()





    


