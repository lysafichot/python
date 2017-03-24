#!/usr/bin/env python
# coding: utf-8

from core.Client import Client



# Master Server
masterServer = Client("", 15558)
masterServer.setPseudo("toto")
rooms = masterServer.sendMessage("rooms")
masterServer.setChannels(rooms)
users = masterServer.getUserInRoom("default")

# Clients Server
for key, user in users.items():
    tcpsocket = Client(user["ip"], user["port"])
    tcpsocket.setPseudo("toto")
    tcpsocket.sendMessage("message", "lol")
