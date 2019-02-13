
import socket

def Main():
    # host IP
    host = "0.0.0.0"
    # port number
    port = 8081

    print(socket.gethostname())

    serverSocket = socket.socket()
    serverSocket.bind((host, port))

    serverSocket.listen(5)

    conn, addr = serverSocket.accept()

    print("connection from: " + str(addr))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("ffrom connected user: " + str(data))

        data = str(data).upper()

        print("sending: " + str(data))
        conn.send(data.encode())

    conn.close()

if __name__ == "__main__":
    Main()