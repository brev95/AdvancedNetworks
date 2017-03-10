########################################################################
# Name: Breven Hettinger
# Course: COSC 4653 - Advanced Networks
# Assignment: #2 - Link-Layer Switch Simulator
# File Name: hettingerTS.py
#
# Description: The traffic simulator auto-generates an unending source
# of link-layer frames and send them at random times to the switch
# simulator from a variety of link-layer nodes to other link-layer nodes
########################################################################

class Packet:
	interfaceNum = 0
	srcMAC = ""
	destMAC = ""
	def init(self):
		self.data = []

from socket import *
from sys import *
from time import sleep
import random
import cPickle as pickle
import numpy

# Check for usage error
if len(argv) != 5:
	print "usage: python hettingerTS.py <IP Address> <Port Number> <Config Filename> <Max Random Interval>"
	quit()

# Variables
ipAddr = argv[1]
port = int(argv[2])
configFileName = argv[3]
maxRandInterval = int(argv[4])
configTable = []

numLines = sum(1 for line in open(configFileName))

configFile = open(configFileName)

for i in range(0, numLines):
	configLine = configFile.readline()
	configTable.append(configLine.split(" "))

for MAC in (i[1] for i in configTable):
	MAC.strip()

#if packet.srcMAC in (j[srcMACAddr] for j in table):

# Set up socket
sock = socket(AF_INET, SOCK_DGRAM)

while(1):
	timeInt = random.randint(0, maxRandInterval)
	
	randLine1 = random.randint(1, numLines) - 1
	randLine2 = random.randint(1, numLines) - 1
	
	packet = Packet()
	packet.interfaceNum = configTable[randLine1][0]
	packet.srcMAC = configTable[randLine1][1]
	packet.destMAC = configTable[randLine2][1]
	
	sendPacket = pickle.dumps(packet)
	
	sock.sendto(sendPacket, (ipAddr, port))
	
	print "Sleeping: " + str(timeInt)
	
	sleep(timeInt)
	


























