from os import path
from Loggers.ConsoleLogger import ConsoleLogger
from Loggers.FileLogger import FileLogger
import struct
import time
import sys
import threading
import socket
import glob


from inspect import currentframe, getframeinfo
HEADER = 1024 

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
CHANGE_NAME_MESSAGE = "!NAME="
FILE_NAME_MESSAGE = "!FILE="
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
clients = {}

logger = FileLogger(path.basename(__file__))


def handle_client(conn, addr):

    print(f"[NEW CONNECTION] {addr} connected.")
    sender = addr
    connected = True
    while connected:
        # wait until you recivce info from the client
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            # data = conn.recv(HEADER).decode(FORMAT)
           
            if msg_length:  # we recieve nothing when we connect the first time
                if(msg_length == "!U_FILE="):
                    uploadFile(conn,sender)

                    continue
                elif(msg_length == "!D_FILE="):
                 
                    sendFile(conn)
                    continue
                
                elif(msg_length == "!LISTF"):
                    listFiles(conn)
                    continue

                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                
                if CHANGE_NAME_MESSAGE in msg:
                    tempName = msg.split(CHANGE_NAME_MESSAGE)[1]
                    print(f"[{sender}] changed their name to {tempName}")

                    sendToAllClients(str.encode(
                        f"[{sender}] changed their name to {tempName}\n"))

                    sender = tempName
                    continue

                

                if(msg == DISCONNECT_MESSAGE):
                    print(f"[{sender}]: DISCONNECTED")

                    sendToAllClients(str.encode(f"[{sender}]: DISCONNECTED\n"))
                    connected = False
                    break
                print(f"[{sender}]: {msg}")


                sendToAllClients(str.encode(f"[{sender}]: {msg}\n"))
        except Exception as e:

            logger.LogToFile(e, getframeinfo(currentframe()).lineno)
            sys.exit()

    del clients[addr]
    conn.close()


def uploadFile(conn,sender):
    msg_length = conn.recv(HEADER).decode(FORMAT)
    msg_length = int(msg_length)
    fileName = conn.recv(msg_length).decode(FORMAT)

    sendToAllClients(str.encode(f"[{sender}]: Uploaded U_{fileName} \n"))
 
    with open("UploadedFiles/U_"+fileName, "w+") as fileRecived:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        fileRecived.write(msg)
      
    

def sendFile(conn):

    msg_length = conn.recv(HEADER).decode(FORMAT)
    msg_length = int(msg_length)
    fileName = conn.recv(msg_length).decode(FORMAT)

    try:
        # Check if the file exists
        content = open(f"UploadedFiles/{fileName}", "r")
        logger.LogToFile("FILE FOUND", getframeinfo(currentframe()).lineno)
        logger.LogToFile(f"Sendings the contents of {fileName}", getframeinfo(currentframe()).lineno)


        conn.send(content.read().encode(FORMAT))

    except:
        logger.LogToFile(f"[{fileName}] File not found.",getframeinfo(currentframe()).lineno)
        conn.send("404: The file you requested does not exist".encode(FORMAT))
        
    finally:
        content.close()


def listFiles(conn):
    path = 'UploadedFiles'

    files = [f for f in glob.glob(path + "**/*.*", recursive=True)]

    for file in files:
        conn.send(("- "+file.split("\\")[1]+"\n").encode(FORMAT))
 




def start():
    server.listen()  # listen for new connections
    logger.LogToFile("Server is listening",
                     getframeinfo(currentframe()).lineno)
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # we will store the address of the new connection and store a sokcet object that will allow us to send info back to that connection
        conn, addr = server.accept()
        clients[addr] = conn
        # we will pass the conenction to handle client and then start the thread
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # tells us how many threads are connected
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")


def sendToAllClients(message):
    for client in clients:
        clients[client].send(message)


print("[STARTING] Server is starting... ")
start()
