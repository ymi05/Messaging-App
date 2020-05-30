from Commands import Commands
from Loggers.FileLogger import FileLogger
from Loggers.ConsoleLogger import ConsoleLogger
from inspect import currentframe, getframeinfo
import os



class FileLister(Commands):
    def __init__(self,client):
        super().__init__(client)
        
        self.logger = FileLogger(os.path.basename(__file__))
        self.loggerC = ConsoleLogger(os.path.basename(__file__))

    
    def requestFileList(self):
        try:
            
            self.client.send(b'!LISTF')

        except:
            self.logger.LogToFile("Unable to connect to server",getframeinfo(currentframe()).lineno)
            return


        

