import socket

s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Socket created")


# binding

s.bind(('', 8081))

# socket in listening mode
s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()

    print("Connection from", addr)

    c.sendall('Connection made'.encode())

    c.close()
