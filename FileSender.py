from Sender import Sender
import socket
from os import path
from Loggers.ConsoleLogger import ConsoleLogger

class FileSender(Sender):
    def __init__(self,client):
        super().__init__(client)
        self.currentFile = path.basename(__file__)

    
    def sendFileToServer(self,filePath):
        filePath = filePath.split("!FILE=")[1]
        if path.exists(filePath):

            messageToBeSent = filePath.encode(self.FORMAT) 
            self.client.send(messageToBeSent)
    
            self.client.shutdown(socket.SHUT_WR)
  
            
            data =  self.client.recv(1024).decode('utf-8')

            print(data)
            # self.client.close()
        else:
            pass


# "cd../../code/projects/messaging app"

