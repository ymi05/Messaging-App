from Loggers.Logger import Logger
import os
from datetime import datetime


class ConsoleLogger(Logger): 
    def __init__(self,currentFile):
        super().__init__(currentFile)

        
    def logToConsole(self,message,lineNumber):
        
        instance = datetime.now()
        print(f"Message: {str(message)}\t--[{self.currentFile} line : {str(lineNumber)}]--\t {str(instance.strftime(self.date_timeFormat))}\n")
