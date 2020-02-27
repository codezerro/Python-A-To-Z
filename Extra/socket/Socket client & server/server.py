# -*- coding: utf-8 -*-
import socket

host='localhost'
port=8080

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(1)

print("The Server is running and is listing to client requests")

con,address = sock.accept()

print("Connection has been established with ",str(address))
message="Hey there is somethings important for you"

con.send(message.encode())

con.close() 