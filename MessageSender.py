from Sender import Sender

class MessageSender(Sender):
    def __init__(self,client):
        super().__init__(client)
    
    def sendMessageToServer(self,message):
        messageToBeSent = message.encode(self.FORMAT) 
        msg_length = len(messageToBeSent)
        msg_length = str(msg_length).encode(self.FORMAT)
        msg_length += b' ' * (self.HEADER - len(msg_length)) 
        self.client.send(msg_length)
        self.client.send(messageToBeSent)

