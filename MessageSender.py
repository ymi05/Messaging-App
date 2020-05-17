class MessageSender():
    def __init__(self,client):
        self.client = client
        self.FORMAT = "utf-8"
        self.HEADER = 64 
    
    def sendMessageToServer(self,message):
        messageToBeSent = message.encode(self.FORMAT)
        msg_length = len(messageToBeSent)
        msg_length = str(msg_length).encode(self.FORMAT)
        msg_length += b' ' * (self.HEADER - len(msg_length))#the byte rep of this string
        self.client.send(msg_length)
        self.client.send(messageToBeSent)