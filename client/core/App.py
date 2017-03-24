
#!/usr/bin/env python
# coding: utf-8

import socket
import uuid
import pickle
from Tkinter import *
import Client

class App(Tk):
    def __init__(self, client):
        self.client = client



        Tk.__init__(self)
        self.title('Chat Bahamas')
        can1 = Canvas(self, bg='white', height=250, width=400).grid(row=1, column=0, columnspan=3)
        # can1.pack(side=TOP)
        self.pseudo = StringVar()

        self.label = Label(self, text="Pseudo")
        self.label.grid(row=2, column=0, columnspan=1)
        self.entry = Entry(self, textvariable=self.pseudo)
        self.entry.grid(row=2, column=1, columnspan=1)
        # self.entry.pack()
        # self.label.pack(padx=1, pady=10)
        self.button = Button(self, text="Get", command=self.on_button)
        self.button.grid(row=2, column=2, columnspan=1)
        # self.button.pack(padx=100, pady=10)

    def on_button(self):

        self.client.setPseudo(self.entry.get())
        self.hello = Label(self, text='Hello')

        self.pseudoDisplay = Label(self, text='', textvariable=self.pseudo)
        self.hello.grid(row=0, column=0, columnspan=1)
        self.pseudoDisplay.grid(row=0, column=1, columnspan=1)
        self.button.grid_forget()
        self.button.grid_forget()
        self.label.grid_forget()
        self.entry.grid_forget()

        self.label = Label(self, text="Send a message")
        self.label.grid(row=2, column=0, columnspan=1)
        self.entry = Entry(self, textvariable=self.pseudo)
        self.entry.grid(row=2, column=1, columnspan=1)
        # self.entry.pack()
        # self.label.pack(padx=1, pady=10)
        self.button = Button(self, text="Get", command=self.on_button)
        self.button.grid(row=2, column=2, columnspan=1)




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