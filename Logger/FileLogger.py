from Logger import Logger
from datetime import datetime
import os
class FileLogger(Logger):
    def __init__(self,currentFile,logFile = "log.txt"):
        super().__init__(currentFile)
        self.filePath = logFile

    def LogToFile(self,message):
        instance = datetime.now()

        f = open(self.filePath, "a")
        f.write(f"Message: {str(message)}\t--[{self.currentFile}]--\t {str(instance.strftime(self.date_timeFormat))}\n")
        f.close()

x = FileLogger(os.path.basename(__file__))
x.LogToFile("Error at line 32")