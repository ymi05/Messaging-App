from Loggers.Logger import Logger
import os
from datetime import datetime
class ConsoleLogger(Logger): 
    def __init__(self,currentFile):
        super().__init__(currentFile)

    def logToConsole(self,message):
        
        instance = datetime.now()
        print(f"Message: {str(message)}\t--[{self.currentFile}]--\t {str(instance.strftime(self.date_timeFormat))}\n")

