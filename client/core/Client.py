#!/usr/bin/env python
# coding: utf-8

import socket
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
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.socket.connect( (self.ip, self.port) )
            print("[+] Nouveau connexion de %s %s" % (self.ip, self.port))

        except Exception as e:
            self.socket.close()
            print("[/!\] Echec de la connexion a %s:%d. Exception is %s" % (self.ip, self.port, e))
            return False

    def setPseudo(self, pseudo):
        self.pseudo = pseudo

    def sendMessage(self, commande, message=""):
        self.connexion()

        try:
            content = {"uniqueId": self.uniqueId, "pseudo": self.pseudo, "type": commande, "message": message}
            self.socket.send(pickle.dumps(content))
            recive = self.socket.recv(1024)
            recive = pickle.loads(recive)

            if recive != "ok":
                return recive
            else:
                return True

        except Exception as e:
            print("[/!\] Imposible d'envoyer le message a %s:%d. Exception est %s" % (self.ip, self.port, e))
            return False

        self.socket.close()

    def setChannels(self, rooms):
        self.rooms = rooms

    def sendMessageToChannel(self, channel, message):

        if self.rooms == "":
            return false

        # room = self.rooms[channel]
        # # for (slug, title) in room:
        # #     print ("ok")


client = Client("", 15558)
client.setPseudo("toto")

rooms = client.sendMessage("rooms")
client.setChannels(rooms)
client.sendMessageToChannel("default", "helo")
