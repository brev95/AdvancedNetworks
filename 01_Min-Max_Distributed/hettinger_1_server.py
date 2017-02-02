########################################################################
# Name: Breven Hettinger
# Course: COSC 4653 - Advanced Networks
# Assignment: #1 - Min-Max_StdDev Distributed Processing
# File Name: hettinger_1_server.py
########################################################################

# Imports
from socket import *
from sys import *
import numpy
from time import sleep
from signal import *
import math

# Create a socket
serverSocket = socket(AF_INET, SOCK_STREAM)


# Variables
port = int(argv[1])
minVal = 1000001
maxVal = 0
stddevAvg = 0.0
numArray = []
dataArray = []


if len(argv) != 2:
	print "Usage: python hettinger_1_server.py <port number>"


# Bind socket
serverSocket.bind(('', port))
serverSocket.listen(1)
conn, addr = serverSocket.accept()


def signalhandler(signal,frame):
	print('killing server')
	conn.close()
	exit()
signal(SIGINT, signalhandler)


# Receive data
while 1:
	#conn, addr = serverSocket.accept()
	data = conn.recv(128).strip()
	#data = int(data)
	print data
	if data=="-1":
		print('exiting')
		break
	else:
		numArray.append(int(data))
		
dat = [str(min(numArray)), str(max(numArray)), str(numpy.std(numArray))]
dat = "_".join(dat)

print dat

conn.sendall(dat)

#serverSocket.sendall(dat)

print "Closing Socket"
		
conn.close()
	
		
# Compute server results
#dat = [str(min(numArray)), str(max(numArray)), str(numpy.std(numArray))]

#print "_".join(dat)

#serverSocket.sendall("_".join(dat))
#serverSocket.sendall("anything")

#sleep(0.05)
#conn.close()










