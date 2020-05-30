from Commands import Commands
from MessageSender import MessageSender
from Loggers.FileLogger import FileLogger
from Loggers.ConsoleLogger import ConsoleLogger
from inspect import currentframe, getframeinfo
import os



class FileRetriver(Commands):
    def __init__(self,client):
        super().__init__(client)
        
        self.logger = FileLogger(os.path.basename(__file__))
        self.loggerC = ConsoleLogger(os.path.basename(__file__))

    
    def requestFile(self,fileName):
        try:
            fileName = fileName.split("!D_FILE=")[1]
    
            messageSender = MessageSender(self.client)
            
            self.client.send(b'!D_FILE=')

        except:
            self.logger.LogToFile("Unable to connect to server",getframeinfo(currentframe()).lineno)
            return

        try:
            messageSender.sendMessageToServer(fileName)               
             

        except:
            self.logger.LogToFile("Unable to request the data.",getframeinfo(currentframe()).lineno)
            return

        

