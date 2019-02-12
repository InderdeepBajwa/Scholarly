import socket

def Main():
    host = '0.0.0.0'
    port = 8081

    clientSocket = socket.socket()
    clientSocket.connect((host,port))

    message = input("Enter a message: ")

    while message != 'end':
        clientSocket.send(message.encode())
        data = clientSocket.recv(1024).decode()

        print ("Received from server: " + data)

        message = input("Enter a message: ")

    clientSocket.close()

    if __name__ == "__main__":
         Main()    

