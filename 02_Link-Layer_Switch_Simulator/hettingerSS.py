########################################################################
# Name: Breven Hettinger
# Course: COSC 4653 - Advanced Networks
# Assignment: #2 - Link-Layer Switch Simulator
# File Name: hettingerSS.py
#
# Description: The switch simulator simulates the actions described for
# a switch in Ch. 5 of Kurose.
########################################################################

class Packet:
	interfaceNum = 0
	srcMAC = ""
	destMAC = ""
	def init(self):
		self.data = []

from socket import *
from sys import *
#from time import *
import time
import cPickle as pickle
import numpy
import datetime

# Check for usage error
if len(argv) != 4:
	print "usage: python hettingerSS.py <Port Number> <Maximum Table Size> <Maximum Aging Time>"
	quit()

# Variables
port = int(argv[1])
maxTableSize = int(argv[2])
maxAgingTime = int(argv[3])
width = 3
table = [] #[[0 for x in range(width)] for x in range(maxTableSize)]
tableFull = False

# Table columns
ifaceNum = 0
srcMACAddr = 1
arrivalTime = 2

# Set up socket
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(("", port))

while(1):
	data, addr = sock.recvfrom(1024)
	
	packet = Packet()
	packet = pickle.loads(data)
	
	if len(table) > maxTableSize:
		tableFull = True
	elif len(table) <= maxTableSize:
		tableFull = False
	
	
	if packet.srcMAC in (j[srcMACAddr] for j in table):
		table[j][arrivalTime] = time.time()
	elif packet.srcMAC in (j[srcMACAddr] for j in table) and tableFull == False:
		table.append[packet.interfaceNum, packet.srcMAC, time.time()]
		print "ADD: Adding MAC address %s on interface %s to switch table" %(packet.srcMAC, packet.interfaceNum)
	elif packet.srcMAC not in (j[srcMACAddr] for j in table) and tableFull == True:
		print "WARNING, Could not add MAC address %s on interface %s to switch table" %(packet.srcMAC. packet.interfaceNum)
	
	
	
	
	
	
	
	#for i in range(maxTableSize):
	#print len (table)
	#for i in table:
	#	if packet.srcMAC in (j[srcMACAddr] for j in table):
	#		table[i][arrivalTime] = time.time()
	#		continue
	#	elif packet.srcMAC not in (j[srcMACAddr] for j in table) and tableFull != True:
			#table[i][ifaceNum] = packet.interfaceNum
			#table[i][srcMACAddr] = packet.srcMAC
			#table[i][arrivalTime] = time.time()
	#		print "ADD: Adding MAC address %s on interface %s to switch table" %(packet.srcMAC, packet.interfaceNum)
	#		continue
	#	elif packet.srcMAC not in (j[srcMACAddr] for j in table) and tableFull == True:
	#		print "WARNING, Could not add MAC address %s on interface %s to switch table" %(packet.srcMAC. packet.interfaceNum)
	#		continue
	
	#table.append([0, 1, 2])
	
	#print table
	

#datetime.datetime.time(datetime.datetime.now())






#	for i in range(maxTableSize):
#		for j in range(width):
#			table[i][j] = "%s,%s"%(i,j)
			


