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

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(('', 15558))

while True:
    tcpsock.listen(100)
    client, address = tcpsock.accept()

    response = client.recv(1024)
    if response != "":
        response = pickle.loads(response)

        # Get infos
        uniqueId = response["uniqueId"]
        commande = response["type"]
        message = response["message"]

        if uniqueId not in user_list:
            print("[+] User add: %s:%d " % (address[0], address[1]))
            user_list[uniqueId] = {'ip': address[0], 'port': 1111}

        # Traitements des commandes + reponse
        if intern(commande) is intern("rooms"):
            client.send(pickle.dumps({"default": user_list}))
        else:
            client.send("ok")

        # On deconnect le client
        client.close()


        print("[i] Message bien recu par le sereur %s" % (response))
