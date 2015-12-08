#!/usr/bin/python
# -*- coding:utf8 -*-
# import MySQLdb
# import sys
# # sys.setdefaultencoding('utf8')
 
# try:
#     conn=MySQLdb.connect(host='localhost',user='root',passwd='1233',db='two_admin',port=3306,charset='utf8')
#     cur=conn.cursor()
#     cont = cur.execute('select username from two_user')
#     data = cur.fetchall()
#     for row in data:
#         print row
#     print conn
#     cur.close()
#     conn.close()
# except MySQLdb.Error,e:
#      print "Mysql Error %d: %s" % (e.args[0], e.args[1])
# -- coding:utf8 --
import Tkinter
import tkMessageBox
from Tkinter import *
top = Tkinter.Tk()
top.title("这是我的")
# tkMessageBox.showinfo("登陆","你还需要登陆!!");最后你想要什么有没有呀....好好的真想不到你还会这个

def hello():
    tkMessageBox.showinfo('Hello World!! 你好,世界',"Hello Python")
    # print 'hello box'

top.geometry("1024x720")
top.resizable(width=False,height=True)

l = Label(top,text="label",bg="green",font=("",16))
l.pack()

Button = Tkinter.Button(top,text="你好呀",command=hello)
Button.pack()

frm = Frame(top)
frm_l = Frame(frm)
Label(frm_l,text="houde",font=('',13)).pack(side=TOP)
Label(frm_l,text="zaiwu",font=('',13)).pack(side=TOP)
frm_l.pack(side=LEFT)


frm_r = Frame(frm)
Label(frm_r,text="houde",font=('',13)).pack(side=TOP)
Label(frm_r,text="zaiwu",font=('',13)).pack(side=TOP)
frm_r.pack(side=RIGHT)

frm.pack()

frm1 = Frame(top)
Label(frm1,text="用户名:",font=('',15)).pack(side=LEFT)

var = StringVar()
e = Entry(frm1,textvariable=var)
e.pack(side=RIGHT)
frm1.pack()
frm2 = Frame(top)
Label(frm2,text="密  码:",font=('',15)).pack(side=LEFT)

vara = StringVar()
s = Entry(frm2,textvariable=var)
s.pack(side=RIGHT)
frm2.pack()

def put():
	print vara.get()

Tkinter.Button(top,text="aaa",command=put).pack()

top.mainloop()

