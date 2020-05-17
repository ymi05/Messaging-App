import socket
import threading

class Client():
    def __init__(self):

        self.PORT = 5050
        self.DISCONNECT_MESSAGE = "!DISCONNECT" 
        self.SERVER = "" #INSERT YOUR LOCAL IP ADDRESS HERE
        self.ADDR = (self.SERVER,self.PORT)

        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect(self.ADDR)



    def getClient(self):
        return self.client

