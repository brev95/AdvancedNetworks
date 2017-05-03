########################################################################
# Name: Breven Hettinger
# Course: COSC 4653 - Advanced Networks
# Assignment: #7 - 
# File Name: hettinger_7_server1.py
########################################################################

# Imports
from socket import *
from sys import *
import wave
import struct


# Create a socket
serverSocket = socket(AF_INET, SOCK_STREAM) # Do I need 2 sockets?


# Variables
port = 5000

# Bind socket
serverSocket.bind(('', port))
serverSocket.listen(1)
conn, addr = serverSocket.accept()

while(1):
	fileLen = conn.recv(1024)
	fileName = conn.recv(1024)
	data = ' '
	while(len(data) < int(fileLen)):
		data = data + conn.recv(1024)
	
	
	byteFile = fileName.split('.', 1)[0] + ".byt"
	w = open(byteFile, 'w')
	
	byteData = data[44:]
	bytestream = [int(struct.unpack("<B", w)[0]) for b in byteData]
	
	pass
	
	
	
	
	
	
	
	
	
	
	
	#waveFile = wave.open(audioFile, 'r')
	length = data.getnframes()

	waveData = waveFile.readframes(length)

	bytestream = [int(struct.unpack("<B", w)[0]) for w in waveData]
	
	data2 = data[44:]
	waveData2 = struct.pack('%sB' % len(data2), *data2)

	waveFile2.setparams((waveFile.getnchannels(), waveFile.getsampwidth(), waveFile.getframerate(), waveFile.getnframes(), waveFile.getcomptype(), waveFile.getcompname()))

	waveFile2.writeframes(waveData2)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
