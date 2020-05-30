import socket
import threading
import time
class Client():
    def __init__(self):

        self.PORT = 5050
        self.DISCONNECT_MESSAGE = "!DISCONNECT" 
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER,self.PORT)

        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

        self.name = self.ADDR



    def getClient(self):
        return self.client

    def changeName(self,newName):
        self.name = newName

    def getClientName(self):
        return self.name
