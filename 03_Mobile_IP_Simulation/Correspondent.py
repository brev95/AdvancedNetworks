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

# Imports
from socket import *
from sys import *
import cPickle as pickle

# Check for usage error
if len(argv) != 3:
	print "usage: python Correspondent.py <HomeAgent IP Address> <Correspondent IP Address>"
	quit()

# Variables
home_agent_ip = argv[1]
own_ip_addr = argv[2]
message = ""

# Set up socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

homeAgentAddress = (home_agent_ip, 7000)
clientSocket.bind((own_ip_addr, 6000))

while(1):
	#packet = Packet()
	print "Type '0' to shutdown the Correspondent\nType '5' to send a message:"
	frameChoice = raw_input("Choice: ")
	if frameChoice == "0": # Shutdown
		packet = Packet()
		packet.frameType = 0
		sendPacket = pickle.dumps(packet)
		print "Shutting down..."
		clientSocket.sendto(sendPacket, homeAgentAddress)
		clientSocket.close()
		quit()
	elif frameChoice == "5": # Send a message to a mobile node
		message = raw_input("Message: ")
		packet = Packet()
		packet.frameType = 5
		packet.ipAddrA = own_ip_addr
		packet.ipAddrB = home_agent_ip
		packet.msg = message
		sendPacket = pickle.dumps(packet)
		print "\nSending message to HomeAgent..."
		clientSocket.sendto(sendPacket, homeAgentAddress)
	else:
		print "The Correspondent cannot send this message type.\n"
		continue;
	
	recvPacket, addr = clientSocket.recvfrom(1024)
	#packet = Packet()
	packet = pickle.loads(recvPacket)
	if packet.frameType == 6:
		print "Mobile Node not registered\n"
	elif packet.frameType == 9:
		print "\nFrom MobileNode: " + packet.msg + "\n"
		
		
		
		
		
		
		
		
		
		
			
	

