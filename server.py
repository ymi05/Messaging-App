import socket 
import threading 

HEADER = 64 

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER,PORT) 
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT" 
CHANGE_NAME_MESSAGE = "!NAME=" 

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR) 
clients = {}
 
def handle_client(conn, addr): 
    print(f"[NEW CONNECTION] {addr} connected.")
    sender = addr
    connected = True
    while connected:
        #wait until you recivce info from the client
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:# we recieve nothing when we connect the first time

            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) 

            if CHANGE_NAME_MESSAGE in msg:
                tempName = msg.split(CHANGE_NAME_MESSAGE)[1]
                print(f"[{sender}] changed their name to {tempName}")
 
                sendToAllClients( str.encode(f"[{sender}] changed their name to {tempName}\n"))
         
                sender = tempName
                continue

            if(msg == DISCONNECT_MESSAGE):
                print(f"[{sender}]: DISCONNECTED")
  
                sendToAllClients(str.encode(f"[{sender}]: DISCONNECTED\n"))
                connected = False
                break
            print(f"[{sender}]: {msg}")

            sendToAllClients(str.encode(f"[{sender}]: {msg}\n"))
    conn.close()

def start():
    server.listen() #listen for new connections
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True: 
        conn, addr = server.accept() # we will store the address of the new connection and store a sokcet object that will allow us to send info back to that connection
        clients[addr] = conn
        thread = threading.Thread(target=handle_client,args=(conn,addr)) #we will pass the conenction to handle client and then start the thread
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}") #tells us how many threads are connected
        
def sendToAllClients(message):
    for client in clients:
        clients[client].send(message)

print("[STARTING] Server is starting... ")
start()