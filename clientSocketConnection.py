
# audio & socket dependencies
import pyaudio
import socket
import sys

# Variable initialization

FORMAT = pyaudio.paInt16
CHANNELS = 3
RATE = 44100
CHUNK = 4096

# Defining socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def makeSocketConnection(userIP, userPort):
    # Socket connection
    s.connect((userIP, userPort))


def getUsername(UserName):
    global USERNAME
    USERNAME = UserName


# Chat implementation here

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

