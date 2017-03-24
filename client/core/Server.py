#!/usr/bin/env python
# coding: utf-8

import socket
import threading

class Server(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port))

    def run(self):

        print("[i] Connection de %s %s" % (self.ip, self.port))

        response = self.clientsocket.recv(2048)
        self.clientsocket.send("ok")

        print("[i] Client déconnecté...")



# while True:
#     tcpsock.listen(100)
#     print( "En écoute...")
#     (clientsocket, (ip, port)) = tcpsock.accept()
#     newthread = ClientThread(ip, port, clientsocket)
#     newthread.start()
