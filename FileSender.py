from Sender import Sender
import socket
from os import path
from Loggers.FileLogger import FileLogger
from Loggers.ConsoleLogger import ConsoleLogger
from inspect import currentframe, getframeinfo
from MessageSender import MessageSender

class FileSender(Sender):
    def __init__(self,client):
        super().__init__(client)

        self.logger = FileLogger(path.basename(__file__))
        self.loggerC = ConsoleLogger(path.basename(__file__))

        

    
    def sendFileToServer(self,filePath):
        filePath = filePath.split("!U_FILE=")[1]
        # Upload a file
        print(f"\nUploading file: {filePath}...")
        try:
            # Check the file exists
            content = open(filePath, "r")
        except:
            self.logger.LogToFile("File not found.",getframeinfo(currentframe()).lineno)
            return
        try:
            # tell the server what to excecute
            self.client.send(b'!U_FILE=')
        except:
            self.logger.LogToFile("Unable to connect to server.",getframeinfo(currentframe()).lineno)
            return
       
        try:
            #! Due to my basic knowledge in sockets , the file transfer is limited and it is done by sending its contents as a regular message and saving
            #! it when it reaches the server
         
            messageSender = MessageSender(self.client)

            if "/" in filePath:
                filePath = filePath.split("/")
                filePath = filePath[len(filePath)-1]
            messageSender.sendMessageToServer(filePath)

            messageSender.sendMessageToServer(content.read())


            content.close()
        except:
            self.logger.LogToFile("Unable to upload file.",getframeinfo(currentframe()).lineno)
            return
        return

# "cd../../code/projects/messaging app"
# x = ConsoleLogger(path.basename(__file__))
# x.logToConsole("Socket has been shutdown",getframeinfo(currentframe()).lineno)