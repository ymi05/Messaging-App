from tkinter import *
from tkinter import scrolledtext
import socket

class MessageApp():
    def __init__(self,master):
        self.master = master
        self.master.title("Message App")
        self.master.geometry('405x230')
        self.txtField = scrolledtext.ScrolledText(self.master,width=47,height=10)

        self.txtField.grid(column=0,row=0)
        self.messageEntry = Entry(self.master,width=40)

        self.messageEntry.grid(column=0, row=8)


        self.sendBtn = Button(self.master, text="Click Me" ,command = lambda: self.send(self.messageEntry.get()))

        self.sendBtn.grid(column=0, row=11)


        self.HEADER = 64 

        self.PORT = 5050
        self.FORMAT = "utf-8"
        self.DISCONNECT_MESSAGE = "!DISCONNECT" 

        self.SERVER = "" #the IP address of the server goes here
        self.ADDR = (self.SERVER,self.PORT)

        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.client.connect(self.ADDR)
        # msg = ""
        # while msg!="!DISCONNECT":
        #     msg = self.messageEntry.get()

          



    def sendMessage(self,message):
        self.txtField.insert(INSERT, message)
        # self.waitForResponse()


    def send(self,msg):
        self.messageEntry.delete(0, END)
        self.messageEntry.insert(0, "")
        self.sendMessage(msg+'\n')
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))#the byte rep of this string
        self.client.send(send_length)
        self.client.send(message)
     
    
    # def waitForResponse(self):
    #     while True:
    #         serverMessage = self.client.recv(1024)
    #         if len(serverMessage) <= 0:
    #             break
    #         serverMessage = serverMessage.decode(self.FORMAT)
    #         self.sendMessage(serverMessage)
def main():

    window = Tk()
    app = MessageApp(window)


    window.mainloop()




if __name__ == "__main__":
    main()
