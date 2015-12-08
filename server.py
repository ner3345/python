#!/usr/bin/env python
#-*- coding: utf-8 -*-
from socket import *
from time import ctime

HOST = "192.168.1.30"
PORT = 8980
BUFFSIZ = 1024
ADDR = (HOST,PORT)
CLIENTLIST = {}
tcpfd = socket(AF_INET,SOCK_STREAM,0)
tcpfd.bind(ADDR)
tcpfd.listen(5)

def dd():
    print "我的端口是:",PORT
try:
    while True:
        print "等待新的连接..."
        tcpclien,addr = tcpfd.accept()
        tcpfd.setblocking(0)
        print "欢迎你,",addr

        while True:
            data = tcpclien.recv(BUFFSIZ)
            if not data:
                break
            tcpclien.send(data)
            if data[:4]=='uid:':
                uid = data[4:]
                if uid in CLIENTLIST :
                    print CLIENTLIST
                else:
                    CLIENTLIST[uid] = tcpclien
            
            print data
            if data=='listuid':
                for x in CLIENTLIST:
                    print 'UID:',x,'addr:',CLIENTLIST[x]
            elif data=='quit':
                break
            elif data=='exit':
                raise Exception("break")
            # tcpclien.close()
    # tcpfd.close()
except Exception, e:
    tcpfd.close()
    print 'exit'

