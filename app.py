from tkinter import *
from tkinter import scrolledtext
from client import Client
from MessageSender import MessageSender
from FileSender import FileSender
import threading
import time

class MessageApp():
    def __init__(self,master):
       

        self.master = master
        self.master.title("Messaging App")
        self.master.geometry('500x330')
        self.txtField = scrolledtext.ScrolledText(self.master,width=59,height=15)

        self.txtField.grid(column=0,row=0)
        self.messageEntry = Entry(self.master,width=40)

        self.messageEntry.grid(column=0, row=8)

    


        self.send_messageBtn = Button(self.master, text="Send Message" ,command = lambda: self.send(self.messageEntry.get()))
        self.send_messageBtn.grid(column=0, row=11)
      
 
        self.FORMAT = "utf-8"
        self.DISCONNECT_MESSAGE = "!DISCONNECT" 
        self.clientObj = Client()
        self.clientObj = self.clientObj.getClient()
        self.messageSender = MessageSender(self.clientObj)
        self.fileSender = FileSender(self.clientObj)
        self.thread = threading.Thread(target=self.waitForResponse)
        self.thread.start()
   


    def printToTextBox(self,message):
        print(message)
        self.txtField.insert(INSERT, message)

     



    def send(self,msg):
        self.messageEntry.delete(0, END)
        self.messageEntry.insert(0, "")
        if("!FILE=") in msg:
            self.fileSender.sendFileToServer(msg)
        else:
            self.messageSender.sendMessageToServer(msg)

        if(self.DISCONNECT_MESSAGE == msg):
            sys.exit()
            self.master.destroy()
        
    
    def waitForResponse(self):
        while True:
            serverMessage = self.clientObj.recv(1024).decode(self.FORMAT)
        
            if len(serverMessage) <= 0:
                break
            self.printToTextBox(serverMessage)
def main():

    window = Tk()
    MessageApp(window)


    window.mainloop()




if __name__ == "__main__":
    main()