'''
Student Name: Nick Faul
Course: COSC 4653 Advanced Networks
Assignment: Mobile IP Simulation
File name: ForeignAgent.py 

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

#Packet Class
class Packet:
	frameType = 0
	ipAddrA = ''
	ipAddrB = ''
	msg = ''
	def init(self):
		self.data = []
		 
#variables
port = 8000
foreignIp = argv[1]
register = False
mobile_ip = ""
home_ip = ""

#creating server socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', port))

while 1:
	data, addr = serverSocket.recvfrom(1024)
	recvpacket = Packet()
	recvpacket = pickle.loads(data)
	sendpacket = Packet()
	
	if recvpacket.frameType == 0: # Receiving Shutdown from Mobile Node and deregistering from ForeignAgent
		register = False
		print 'Mobile Node shutting down...\n'
		
	elif recvpacket.frameType == 1: #Registering Mobile Node with Foreign Agent and notifying Home Agent
		register = True
		print 'Mobile Node registered with Foreign Agent...\n'
		mobile_ip = recvpacket.ipAddrA
		home_ip = recvpacket.ipAddrB
		sendpacket.frameType = 3
		sendpacket.ipAddrA = foreignIp
		sendpacket.ipAddrB = home_ip
		serialpacket = pickle.dumps(sendpacket)
		homeAddress = (home_ip, 7000)
		serverSocket.sendto(serialpacket, homeAddress)
	
	elif recvpacket.frameType == 2: # Receiving dereg and notifying the Home Agent
		register = False
		print 'Mobile Node deregister from Foreign Agent...\n'
		mobile_ip = recvpacket.ipAddrA
		home_ip = recvpacket.ipAddrB
		sendpacket.frameType = 4
		sendpacket.ipAddrA = foreignIp
		sendpacket.ipAddrB = home_ip
		serialpacket = pickle.dumps(sendpacket)
		homeAddress = (home_ip, 7000)
		serverSocket.sendto(serialpacket, homeAddress)
		
	elif recvpacket.frameType == 7: #Receiving from Home Agent and sending to Mobile Node
		print 'Message recieved from Home Agent...\n'
		msg = recvpacket.msg
		sendpacket.msg = msg
		sendpacket.frameType = 8
		sendpacket.ipAddrA = recvpacket.ipAddrA
		serialpacket = pickle.dumps(sendpacket)
		mobileAddress = (mobile_ip, 9000)
		serverSocket.sendto(serialpacket, mobileAddress)
		print 'Message sent to Mobile Node...\n'
		
	
	

