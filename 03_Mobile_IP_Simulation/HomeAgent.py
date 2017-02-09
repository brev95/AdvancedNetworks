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

# Imports
from socket import *
from sys import *

# Create a socket
serverSocket = socket(AF_INET, SOCK_STREAM)


# Variables
corr_ip_addr = args[1]
own_ip_addr = args[2]
message = ""
frameChoice = 0

# Bind socket
serverSocket.bind((own_ip_addr, 7000))
serverSocket.listen(1)
conn, addr = serverSocket.accept()

def signalhandler(signal,frame):
	print('killing server')
	conn.close()
	exit()
signal(SIGINT, signalhandler)

while(1):
	message = conn.recvfrom(1024)
	if message = '0':
		conn.close()
	if message = '5':
		
switch(frameChoice):
		#case 0: # Shutdown
			
		#case 1: # Register a mobile node with a foreign agent
			
		#case 2: # Deregister a mobile node with a foreign agent
			
		#case 3: # Register a mobile node with a home agent
			
		#case 4: # Deregister a mobile node with a home agent
			
		#case 5: # Send a message to a mobile node
			
		case 6: # Imform correspondent that no mobile node with that permanent IP address is registered
			
		case 7: # Send a message to a mobile node
			
		#case 8: # Send a message to a mobile node
			
		#case 9: # Send a message to a correspondent
			
		default:
			print "The Correspondent cannot send this message type.\n"
