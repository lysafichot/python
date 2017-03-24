#!/usr/bin/env python
# coding: utf-8

from Tkinter import *
from Client import Client

class App(Tk):
    def __init__(self, client):
        self.client = client

        Tk.__init__(self)
        self.title('Chat Bahamas')
        can1 = Canvas(self, bg='white', height=250, width=400).grid(row=1, column=0, columnspan=3)
        self.pseudoInput = StringVar()

        self.pseudoLabel = Label(self, text="Pseudo")
        self.pseudoLabel.grid(row=2, column=0, columnspan=1)
        self.pseudoEntry = Entry(self, textvariable=self.pseudoInput)
        self.pseudoEntry.grid(row=2, column=1, columnspan=1)

        self.button = Button(self, text="Get", command=self.sendPseudo)
        self.button.grid(row=2, column=2, columnspan=1)


    def sendMessage(self):
        self.msg = self.messageInput.get()
        print(self.msg)

        if self.userList != False:
            for key, user in self.userList.items():
                tcpsocket = Client(user["ip"], user["port"])
                tcpsocket.setPseudo(self.pseudo)
                tcpsocket.sendMessage("message", self.msg)

    def sendPseudo(self):

        self.pseudo = self.pseudoEntry.get()

        masterServer = Client("", 15558)
        masterServer.setPseudo(self.pseudo)

        rooms = masterServer.sendMessage("rooms")
        masterServer.setChannels(rooms)
        self.userList = masterServer.getUserInRoom("default")

        self.hello = Label(self, text='Hello')

        self.pseudoDisplay = Label(self, text='', textvariable=self.pseudoInput)
        self.hello.grid(row=0, column=0, columnspan=1)
        self.pseudoDisplay.grid(row=0, column=1, columnspan=1)
        self.button.grid_forget()
        self.button.grid_forget()
        self.pseudoLabel.grid_forget()
        self.pseudoEntry.grid_forget()

        self.messageInput = StringVar()

        self.messageLabel = Label(self, text="Send a message")
        self.messageLabel.grid(row=2, column=0, columnspan=1)
        self.messageEntry = Entry(self, textvariable=self.messageInput)
        self.messageEntry.grid(row=2, column=1, columnspan=1)

        self.sendButton = Button(self, text="Get", command=self.sendMessage)
        self.sendButton.grid(row=2, column=2, columnspan=1)




app = App(Client("", 15558))
app.mainloop()

        # room = self.rooms[channel]
        # # for (slug, title) in room:
        # #     print ("ok")


        # interface = Interface()
        # lst = ['a', 'b', 'c', 'd']
        #
        # root = Tk()
        # t = Text(root)
        # for x in lst:
        #     t.insert(END, x + '\n')
        # t.pack()
        # root.mainloop()

# client = Client("", 15558)
# Interface(Client("", 15558))
# client.setPseudo("toto")
#
# rooms = client.sendMessage("rooms")
# client.setChannels(rooms)
# client.sendMessageToChannel("default", "helo")