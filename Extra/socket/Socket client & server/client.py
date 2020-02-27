# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:34:39 2019

@author: CodeZerro
"""
import socket

host='localhost'
port=8080

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((host,port))

message=sock.recv(1024)

while message:
    
    print("Message : ",message.decode())
    message=sock.recv(1024)

sock.close()