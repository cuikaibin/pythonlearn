#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

s = socket.socket()

host = '172.24.133.33'
port = 8080

s.connect((host, port))
#接收数据，1024最大字节数
print s.recv(1024)