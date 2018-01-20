# import socket
#
# tcpClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# tcpClient.connect(("127.0.0.1",23457))
#
# while True:
#     data = raw_input('>_')
#     if not data:
#         break
#     tcpClient.send(data)
#     recvData = tcpClient.recv(1024)
#     print recvData
# print "========"
# tcpClient.close()

import socket

HOST = "127.0.0.1"
PORT = 23456
BUFSIZ = 1024

clie = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clie.connect((HOST,PORT))
while True:
    data = raw_input("=:")
    clie.send(data)
    recData =  clie.recv(BUFSIZ)
    if  recData == '0':
    	print "out of service"
        break
    print recData
clie.close()