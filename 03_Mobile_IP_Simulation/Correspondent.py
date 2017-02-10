########################################################################
# Name: Breven Hettinger/Nick Faul
# Course: COSC 4653 - Advanced Networks
# Assignment: #3 - Mobile IP Simulation
# File Name: Correspondent.py
#
# Description: An interactive program that allows a user to send a
#  and receive the response. It handles specific message types listed in
#  the Frame Format section. When the Correspondent program is exchanging
#  messages with the mobile node, it shall always send a message to the
#  IP address of the home agent. It does this even though it can obtain 
#  the current IP address of the mobile node from the UDP packet that the
#  mobile node sends it.
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

# Variables
message = ""

# Set up socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

home_agent_ip = argv[1]

server_address = (home_agent_ip, 6000)
clientSocket.connect(server_address)

while(1):
	print "Type '0' to shutdown the home agent\nType '5' to send a message:\n"
	frameChoice = raw_input("Choice: ")
	if frameChoice == "0": # Shutdown
		packet = Packet()
		packet.frameType = 0
		clientSocket.sendto(str(packet), (home_agent_ip))
		
	elif frameChoice == "5": # Send a message to a mobile node
		print "Type your message: "
		message = raw_input("Message: ")
		packet = Packet()
		packet.fieldType = 5
		packet.ipAddrA = "10.0.0.5"
		packet.ipAddrB = "10.0.0.4" # Figure out what to do with ip addresses
		clientSocket.sendto(str(packet), (home_agent_ip))
		
	else:
		print "The Correspondent cannot send this message type.\n"
	
	packet = clientSocket.recvfrom(1024)
	str_to_class(packet)
	print packet.msg
	
			
	

