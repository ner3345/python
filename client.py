#!/usr/bin/env python
#-*- coding: utf-8 -*-
from socket import *
from time import ctime

HOST = "192.168.1.30"
PORT = 8980
BUFFSIZE = 1024
ADDR = (HOST,PORT)
TMP = 0
cfd = socket(AF_INET,SOCK_STREAM,0)

cfd.connect(ADDR)

while True:

    if TMP==0:
        data = raw_input('输入你的ID> ')
        if not data:
            break
        TMP = int(data)
        cfd.send("uid:"+data)
    else:
        data = raw_input(str(TMP)+'> ')
        cfd.send(data)
    data = cfd.recv(BUFFSIZE)
    if not data:
        break
    print data
    if data=='quit' or data=='exit':
        break
cfd.close()
