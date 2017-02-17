########################################################################
# Name: Breven Hettinger/Nick Faul
# Course: COSC 4653 - Advanced Networks
# Assignment: #3 - Mobile IP Simulation
# File Name: HomeAgent.py
#
# Description: This program shall receive a message from a foreign agent
#  to register/deregister a mobile node, shall receive a message from 
#  a correspondent to send to a mobile node, and shall forward a message
#  from a correspondent to a mobile node by way of a foreign agent.
#
########################################################################

class Packet:
	frameType = 0
	ipAddrA = ""
	ipAddrB = ""
	msg = ""
	def init(self):
		self.data = []

# Imports
from socket import *
from sys import *
import cPickle as pickle

# Check for usage error
if len(argv) != 3:
	print "usage: python HomeAgent.py <Correspondent IP Address> <HomeAgent IP Address>"
	sys.exit()

# Variables
corr_ip_addr = argv[1]
own_ip_addr = ""
message = ""
frameChoice = 0
mobileRegistered = False

mobile_ip_addr = ""
foreign_ip_addr = ""

# Create a socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind socket
serverSocket.bind((own_ip_addr, 7000))

while(1):
	recvPacket, addr = serverSocket.recvfrom(1024)
	#packet = Packet()
	packet = pickle.loads(recvPacket)
	#print packet
	print "Packet type: " + str(packet.frameType)
	if packet.frameType == 0: # Shutdown
		print "Correspondent shutting down..."
	elif packet.frameType == 3: # Register a mobile node
		print "Mobile Node registered..."
		mobileRegistered = True
		foreign_ip_addr = packet.ipAddrA
		mobile_ip_addr = packet.ipAddrB
	elif packet.frameType == 4: # Deregister a mobile node
		print "MobileNode deregistered..."
		mobileRegistered = False
		mobile_ip_addr = ""
	elif packet.frameType == 5: # Send a message to a mobile node
		print "Received message from Correspondent"
		if mobileRegistered == True:
			print "Mobile Registered"
			sendPacket = Packet()
			sendPacket.frameType = 7
			sendPacket.ipAddrA = packet.ipAddrA
			sendPacket.ipAddrB = foreign_ip_addr
			sendPacket.msg = packet.msg
			sentPacket = pickle.dumps(sendPacket)
			serverSocket.sendto(sentPacket, (foreign_ip_addr, 8000))
		else:
			print "Mobile not registered"
			sendPacket = Packet()
			sendPacket.frameType = 6
			sendPacket.ipAddrB = own_ip_addr
			sendPacket.msg = "Mobile node is not currently registered."
			sentPacket = pickle.dumps(sendPacket)
			serverSocket.sendto(sentPacket, (corr_ip_addr, 6000))
	else:
		print "The HomeAgent cannot receive this message type.\n"
		
		
		
		
		
		
		
		
		
		
