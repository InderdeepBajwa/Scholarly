
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
