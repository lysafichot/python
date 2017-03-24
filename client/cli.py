#!/usr/bin/env python
# coding: utf-8

import socket
from core.Client import Client
from core.Server import Server

speudoIsEmpty = True
global pseudo
global users

pseudo = ""

def sendMessage(message):

    if users != False:
        for key, user in users.items():
            tcpsocket = Client(user["ip"], user["port"])
            tcpsocket.setPseudo(pseudo)
            tcpsocket.sendMessage("message", message)


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

while True:

    print ("Votre message")
    message = raw_input()
    sendMessage(message)
