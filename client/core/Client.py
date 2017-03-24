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
            print("[+] Nouveau connexion a %s %s" % (self.ip, self.port))

        except Exception as e:
            self.socket.close()
            print("[/!\] Echec de la connexion a %s:%d. L'exception est : %s" % (self.ip, self.port, e))
            return False

    def setPseudo(self, pseudo):
        self.pseudo = pseudo

    def sendMessage(self, commande, message=""):
        self.connexion()

        try:
            content = {"uniqueId": self.uniqueId, "pseudo": self.pseudo, "type": commande, "message": message}
            self.socket.send(pickle.dumps(content))
            recive = self.socket.recv(999999)

            if recive != "ok":
                return pickle.loads(recive)
            else:
                return True

        except Exception as e:
            print("[/!\] Imposible d'envoyer le message a %s:%d. Exception est : %s" % (self.ip, self.port, e))
            return False

        self.socket.close()

    def setChannels(self, rooms):
        self.rooms = rooms

    def getUserInRoom(self, room):

        if self.rooms == "":
            return false

        return self.rooms[room]
