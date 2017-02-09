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

# Imports
from socket import *
from sys import *

# Variables
frameChoice = 0
message = ""
frame_field = ""

# Set up socket
clientSocket = socket(AF_INET, SOCK_STREAM)

home_agent_ip = args[1]

server_address = (home_agent_ip, 6000)
clientSocket1.connect(server_address)

while(1):
	print "Type '0' to shutdown the home agent\n Type '5' to send a message\n: "
	frameChoice = raw_input
	switch(frameChoice):
		case 0: # Shutdown
			frame_field = ["0", "", "", "Shutdown"]
			frame_field = "_".join(frame_field)
			clientSocket.sendto(frame_field))
			break;
		#case 1: # Register a mobile node with a foreign agent
			
		#case 2: # Deregister a mobile node with a foreign agent
			
		#case 3: # Register a mobile node with a home agent
			
		#case 4: # Deregister a mobile node with a home agent
			
		case 5: # Send a message to a mobile node
			print "Type your message: "
			message = raw_input
			frame_field = ["5", "10.0.0.5", "10.0.0.4", message] # Need to figure out how to find the IP addresses
			frame_field = "_".join(frame_field)
			clientSocket.sendto(frame_field)
			break;
		#case 6: # Imform correspondent that no mobile node with that permanent IP address is registered
			
		#case 7: # Send a message to a mobile node
			
		#case 8: # Send a message to a mobile node
			
		#case 9: # Send a message to a correspondent
			
		default:
			print "The Correspondent cannot send this message type.\n"
	
	frame_field = clientSocket.recvfrom(1024)
	ret_msg = frame_field.split("_")
	print ret_msg[3]
	
			
	

