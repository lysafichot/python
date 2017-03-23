#!/usr/bin/env python
# coding: utf-8

import socket
import signal
import sys
import pickle

user_list = {}

def signal_handler(signal, frame):
    print('Closing connexion')
    sys.exit(0)

class Server:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        # Start server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.bind((self.ip, self.port))

signal.signal(signal.SIGINT, signal_handler)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15558))

while True:
    socket.listen(5)
    client, address = socket.accept()

    response = client.recv(1024)
    if response != "":
        response = pickle.loads(response)

        # Get infos
        uniqueId = response["uniqueId"]
        type = response["type"]
        message = response["message"]

        if uniqueId not in user_list:
            print("[i] Connexion infos: %s:%d " % (address[0], address[1]))
            user_list[uniqueId] = address[0]

        print("[i] response infos: %s - %s - %s " % (uniqueId, type, message))
        client.send("ok")

print "Close"
client.close()
stock.close()
