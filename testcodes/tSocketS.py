# import socket
#
# HOST = ""
# PORT = 23457
# ADDR = (HOST, PORT)
#
# tcpServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# tcpServer.bind(ADDR)
# tcpServer.listen(5)
#
# while True:
#     print"server is ready!"
#     tcpClient,addr = tcpServer.accept()
#     while True:
#         data = tcpClient.recv(1024)
#         if not data:
#             print 'connection with %s is over',addr
#             tcpClient.send("out of service!")
#             break
#         print data
#         tcpClient.send("get message %s"%data)
#     tcpClient.close()

import socket

HOST = "127.0.0.1"
PORT = 23456
BUFSIZ = 1024

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((HOST,PORT))
serv.listen(5)

while True:
    print "server is ready\n"
    clie,addr = serv.accept()
    print "connet with addr:%d",addr
    while True:
        data = clie.recv(BUFSIZ)
        print data
        if data == "shut down":
            clie.send("0")
            break
        clie.send("got:%s"%data)
    clie.close()
    print "connet with addr:%d is over",addr
serv.close()