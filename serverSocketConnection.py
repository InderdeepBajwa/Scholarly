
import socket
from threading import Thread

def acceptIncomingConnection():
    while True:
        client, clientAddress = serversocket.accept()
        print("%s:%s has connected" % clientAddress)
        client.send(bytes("Connection made", "utf8"))
        addresses[client] = clientAddress
        Thread(target=handleClient, args=(client,)).start()

def handleClient(client):

    name = client.recv(BUFSIZ).decode("utf8")

    welcomeMsg = "Welcome %s!" & name

    client.send(bytes(welcomeMsg, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("&s has left the chat." % name, "utf8"))
            break

def broadcast(msg, prefix=""):

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


clients = {}
addresses = {}

