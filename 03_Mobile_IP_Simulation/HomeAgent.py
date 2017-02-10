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

def str_to_class(str):
    return getattr(sys.modules[__name__], str)

# Imports
from socket import *
from sys import *

# Create a socket
serverSocket = socket(AF_INET, SOCK_DGRAM)


# Variables
corr_ip_addr = argv[1]
own_ip_addr = argv[2]
message = ""
frameChoice = 0
mobileRegistered = False
frame_field = []

# Bind socket
serverSocket.bind((own_ip_addr, 7000))

while(1):
	packet, addr = serverSocket.recvfrom(1024)
	str_to_class(packet)
	if packet.frameType == 0: # Shutdown
		print "Shutting down"
		quit()
		
	elif packet.frameType == 5: # Send a message to a mobile node
		print "Received message from Correspondent"
		if mobileRegistered == True:
			print "hi"
		else:
			packet.ipAddrA = "10.0.0.5"
			packet.ipAddrB = "10.0.0.4"
			packet.msg = "Mobile node is not currently registered."
			conn.sendto(packet)
		
	else:
		print "The Correspondent cannot send this message type.\n"
		
		
		
#switch(frameChoice):
		#case 0: # Shutdown
			
		#case 1: # Register a mobile node with a foreign agent
			
		#case 2: # Deregister a mobile node with a foreign agent
			
		#case 3: # Register a mobile node with a home agent
			
		#case 4: # Deregister a mobile node with a home agent
			
		#case 5: # Send a message to a mobile node
			
		#case 6: # Imform correspondent that no mobile node with that permanent IP address is registered
			
		#case 7: # Send a message to a mobile node
			
		#case 8: # Send a message to a mobile node
			
		#case 9: # Send a message to a correspondent
			
		#default:
		#	print "The Correspondent cannot send this message type.\n"
		#	break;
