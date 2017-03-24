#!/usr/bin/env python
# coding: utf-8

from core.Server import Server
import socket

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(('', 1111))

while True:
    tcpsock.listen(100)
    print( "En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = Server(ip, port, clientsocket)
    newthread.start()
