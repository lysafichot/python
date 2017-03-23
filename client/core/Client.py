#!/usr/bin/env python
# coding: utf-8

import socket
import signal
import sys
import uuid
import pickle

class Client:

    def __init__(self, ip, port):

        self.ip = ip
        self.port = port
        self.uniqueId = uuid.uuid4()

    def connexion (self):

        # Connexion au client
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.socket.connect( (self.ip, self.port) )
            print("[+] Nouveau connexion de %s %s" % (self.ip, self.port))

        except Exception as e:
            self.socket.close()
            print("[!] Echec de la connexion a %s:%d. Exception is %s" % (self.ip, self.port, e))
            return False

    def sendMessage(self, type, message):
        self.connexion()

        try:
            message = pickle.dumps({"uniqueId": self.uniqueId, "type": type, "message": message})
            self.socket.send(message)
            recive = self.socket.recv(1024)
            print("[+] Message du server %s" % (recive))

        except Exception as e:
            print("[!] Imposible d'envoyer le message a %s:%d. Exception est %s" % (self.ip, self.port, e))
            return False

        self.socket.close()

def signal_handler(signal, frame):
    print('[!] Closing connexion')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

client = Client("", 15558)
client.sendMessage("list", "toto")
client.sendMessage("list", "toto")
