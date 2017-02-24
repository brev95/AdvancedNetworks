'''
Student Name: Nick Faul
Course: COSC 4653 Advanced Networks
Assignment: Mobile IP Simulation
File name: MobileNode.py 

Program's Limitations: 
Development Computer: Personal PC
Operating System: Windows 10
Integrated Development Environment (IDE): Notepad++
Compiler: Command Prompt
Program's Operational Status: Working
'''

from socket import *
from sys import *
import cPickle as pickle

#Packet class
class Packet:
	frameType = 0
	ipAddrA = ''
	ipAddrB = ''
	msg = ''
	def init(self):
		self.data = []

#variables
port = 9000
home_ip = argv[1]
foreign_ip = argv[2]
frametype = 0
correspondent_ip = ''
#Creating a socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
foreignAgent = (foreign_ip, 8000)

#Creating Packet
packet = Packet()
inPacket = Packet()
#Menu Loop
ans=True
while ans:
	
	print ("""
    1.Shutdown mobile node
    2.Register with foreign agent
    3.Deregister with foreign agent
    """)
#    4.Send a message to the correspondent
	ans=raw_input("What would you like to do? \n")
	if ans == "1":
	#setting frametype 0 info
		frametype = 0
		packet.frameType = frametype
		serialpack = pickle.dumps(packet)
		clientSocket.sendto(serialpack, foreignAgent)
		print("\nShutdown completed")
		clientSocket.close()
		quit()		
	elif ans == "2":
	#setting frametype 1 info
		frametype = 1
		packet.frameType = frametype
		packet.ipAddrA = home_ip
		packet.ipAddrB = home_ip
		serialpack = pickle.dumps(packet)
		clientSocket.sendto(serialpack, foreignAgent)
		print("\nRegistration complete")
	elif ans == "3":
	#setting frametype 2 info
		frametype = 2
		packet.frameType = frametype
		packet.ipAddrA = home_ip
		packet.ipAddrB = home_ip
		serialpack = pickle.dumps(packet)
		clientSocket.sendto(serialpack, foreignAgent)
		print("\nDeregistration complete")
#	elif ans ==  "4":
#		frametype = 9
#		msg = raw_input("What would you like to send?\n")
#		packet.frameType = frametype
#		packet.msg = msg
#		serialpack = pickle.dumps(packet)
#		clientSocket.sendto(serialpack, (correspondent_ip, 6000))
#		print("\n Message sent to correspondent")
	elif ans != "":
		print("\n Not Valid Choice Try again")

	#Create correspondent socket
	correspondentSocket = socket(AF_INET, SOCK_DGRAM)
	correspondentSocket.bind(('', 9000))
	serialinput, addr = correspondentSocket.recvfrom(1024)
	recvpacket = Packet()
	recvpacket = pickle.loads(serialinput)
	
	print recvpacket.msg

	if recvpacket.frameType == 8:
		reply = raw_input("Reply message: \n")
		replypack = Packet()
		replypack.frameType = 9
		replypack.msg = reply
		correspondent_ip = recvpacket.ipAddrA
		replypack.ipAddrA = recvpacket.ipAddrA
		serialreply = pickle.dumps(replypack)
		clientSocket.sendto(serialreply, (replypack.ipAddrA, 6000))
	
	
	
	

