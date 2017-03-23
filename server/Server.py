#!/usr/bin/env python
# coding: utf-8

import socket
import pickle

user_list = {}
class Server:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        # Start server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.bind((self.ip, self.port))

socketTcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketTcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketTcp.bind(('', 15558))

while True:
    socketTcp.listen(5)
    client, address = socketTcp.accept()

    response = client.recv(1024)
    if response != "":
        response = pickle.loads(response)

        # Get infos
        uniqueId = response["uniqueId"]
        type = response["type"]
        message = response["message"]

        if uniqueId not in user_list:
            print("[+] User add: %s:%d " % (address[0], address[1]))
            user_list[uniqueId] = address[0]

        print("[i] Message bien recu par le sereur %s" % (response))
        # Reponse aux client + deconnexion
        client.send("ok")
        client.close()
