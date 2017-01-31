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

# Receive data
while 1:
	data = conn.recv(1024)
	print data
	if data == "-1":
		break
	else:
		numArray.append(int(data))
	

# Compute server results
dat = [str(min(numArray)), str(max(numArray)), str(numpy.std(numArray))]

print "_".join(dat)

serverSocket.sendall("_".join(dat))
#serverSocket.sendall("anything")
conn.close()










