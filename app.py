from tkinter import *
from tkinter import scrolledtext
from client import Client
from MessageSender import MessageSender
import threading
import time

class MessageApp():
    def __init__(self,master):
        self.clientObj = Client()
        self.clientObj = self.clientObj.getClient()
        self.sender = MessageSender(self.clientObj)

        self.master = master
        self.master.title("Message App")
        self.master.geometry('405x230')
        self.txtField = scrolledtext.ScrolledText(self.master,width=47,height=10)

        self.txtField.grid(column=0,row=0)
        self.messageEntry = Entry(self.master,width=40)

        self.messageEntry.grid(column=0, row=8)

  


        self.sendBtn = Button(self.master, text="Send Messages" ,command = lambda: self.send(self.messageEntry.get()))
        self.sendBtn.grid(column=0, row=11)

 
        self.FORMAT = "utf-8"
        self.DISCONNECT_MESSAGE = "!DISCONNECT" 

        self.thread = threading.Thread(target=self.waitForResponse)
        self.thread.start()
   


    def printToTextBox(self,message):
        self.txtField.insert(INSERT, message)

     



    def send(self,msg):
        self.messageEntry.delete(0, END)
        self.messageEntry.insert(0, "")
        self.sender.sendMessageToServer(msg)

        if(self.DISCONNECT_MESSAGE == msg):
            sys.exit()
            self.master.destroy()
        
    
    def waitForResponse(self):
        while True:
            serverMessage = self.clientObj.recv(1024)
        
            if len(serverMessage) <= 0:
                break
            serverMessage = serverMessage.decode(self.FORMAT)
            self.printToTextBox(serverMessage)
def main():

    window = Tk()
    MessageApp(window)


    window.mainloop()




if __name__ == "__main__":
    main()