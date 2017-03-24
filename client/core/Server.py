#!/usr/bin/env python
# coding: utf-8

import socket
import threading
import pickle

class Server(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port))

    def run(self):

        print("[i] Connection de %s %s" % (self.ip, self.port))

        response = self.clientsocket.recv(999999)
        response = pickle.loads(response)

        print ("[i] New message de %s:" % (response['pseudo']))
        print (response['message'])
        self.clientsocket.send("ok")

        print("[i] Client déconnecté...")
