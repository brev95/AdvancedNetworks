########################################################################
# Name: Breven Hettinger
# Course: COSC 4653 - Advanced Networks
# Assignment: #1 - Min-Max_StdDev Distributed Processing
# File Name: hettinger_1_client.py
########################################################################

# Imports
from socket import *
from sys import *
import random
import numpy
import math
from time import sleep


# Create a socket
clientSocket1 = socket(AF_INET, SOCK_STREAM)
clientSocket2 = socket(AF_INET, SOCK_STREAM)
clientSocket3 = socket(AF_INET, SOCK_STREAM)


# Variables
nums = int(argv[1])
ip1 = argv[2]
port1 = int(argv[3])
ip2 = argv[4]
port2 = int(argv[5])
ip3 = argv[6]
port3 = int(argv[7])
numArray = []
minValue = []
maxValue = []
array1 = []
array2 = []
array3 = []
stddev = []
minVal = 1000001
maxVal = 0
stddevAvg = 0.0
returnVal1 = []
returnVal2 = []
returnVal3 = []


# Check for correct allowable amount of numbers
if len(argv) != 8:
	print "Usage: python hettinger_1_client.py <#integers> <First IP address> <First port number> <Second IP address> <Second port number> <Third IP address> <Third port number>"
	quit


# Randomly generate numbers
for i in range(0, nums):
	numArray.append(random.randrange(1, 1000000))
		
print numArray


# Connect sockets to ports
server_address_1 = (ip1, port1)
clientSocket1.connect(server_address_1)

server_address_2 = (ip2, port2)
clientSocket2.connect(server_address_2)

server_address_3 = (ip3, port3)
clientSocket3.connect(server_address_3)


# Send packets
for i in range(0, nums):
	if i % 3 == 1:
		clientSocket1.send(str(numArray[i]))
		sleep(0.05)
	elif i % 3 == 2:
		clientSocket2.send(str(numArray[i]))
		sleep(0.05)
	elif i % 3 == 0:
		clientSocket3.send(str(numArray[i]))
		sleep(0.05)


# Send -1 and parse received data
clientSocket1.send(str(-1))
sleep(0.05)
message1 = clientSocket1.recv(1024)
print message1
returnVal1 = message1.split("_")
clientSocket1.close()

clientSocket2.send(str(-1))
sleep(0.05)
message2 = clientSocket2.recv(1024)
returnVal2 = message2.split("_")
clientSocket2.close()

clientSocket3.send(str(-1))
sleep(0.05)
message3 = clientSocket3.recv(1024)
returnVal3 = message3.split("_")
clientSocket3.close()

print returnVal1
print returnVal2
print returnVal3



minVal = min(int(returnVal1[0]), int(returnVal2[0]), int(returnVal3[0]));
maxVal = max(int(returnVal1[1]), int(returnVal2[1]), int(returnVal3[1]));
stddevAvg = math.sqrt(float(returnVal1[2]) ** 2 + float(returnVal2[2]) ** 2 + float(returnVal3[2]) ** 2)


# Print server results
print "Results computed by the client from data sent by the servers:\n\n"
print "Minimum value: " + str(minVal)
print "Maximum value: " + str(maxVal)
print "Standard deviation value: " + str(stddevAvg)

print "\n\n"


# Reset variables
minVal = 1000001
maxVal = 0
stddevAvg = 0.0


# Compute client results
for i in range(0, nums):
	if numArray[i] < minVal:
		minVal = numArray[i]
		
for i in range(0, nums):
	if numArray[i] > maxVal:
		maxVal = numArray[i]

stddevAvg = numpy.std(numArray)

print "Test results computed only by the client\n\n"
print "Minimum value: " + str(minVal)
print "Maximum value: " + str(maxVal)
print "Standard deviation value: " + str(stddevAvg)
















