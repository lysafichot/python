#!/usr/bin/env python
# coding: utf-8

from core.Client import Client
from core.Server import Server

speudoIsEmpty = True
pseudo = ""

while speudoIsEmpty:

    print ("Votre pseudo:")
    pseudo = raw_input()

    if pseudo != "":
        speudoIsEmpty = False
    else:
        print ("[i] Pseudo non valide !")

# Master Server
masterServer = Client("", 15558)
masterServer.setPseudo(pseudo)

rooms = masterServer.sendMessage("rooms")
masterServer.setChannels(rooms)
users = masterServer.getUserInRoom("default")

if users != False:

    # Clients Server
    for key, user in users.items():
        tcpsocket = Client(user["ip"], user["port"])
        tcpsocket.setPseudo("toto")
        tcpsocket.sendMessage("message", "lol")
