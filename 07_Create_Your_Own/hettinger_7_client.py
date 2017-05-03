########################################################################
# Name: Breven Hettinger
# Course: COSC 4653 - Advanced Networks
# Assignment: #7 - 
# File Name: hettinger_7_client.py
########################################################################

# Imports
from socket import *
from sys import *
from os import path, stat
from pathlib import Path


# Create sockets
clientSocket1 = socket(AF_INET, SOCK_STREAM)
clientSocket2 = socket(AF_INET, SOCK_STREAM)


# Check for correct allowable amount of numbers
if len(argv) != 5:
	print("Usage: python hettinger_7_client.py <First IP Address> <First Port> <Second IP Address> <Second Port>")
	exit(1)


# Variables
ip1 = argv[1]
port1 = int(argv[2])
ip2 = argv[3]
port2 = int(argv[4])


# Connect sockets to ports
server_address_1 = (ip1, port1)
clientSocket1.connect(server_address_1)

#server_address_2 = (ip2, port2)
#clientSocket2.connect(server_address_2)

while(1):
	# Print menu
	print("Type '1' to send an audio file")
	print("Type '2' to play an audio file")
	print("Type 'q' to quit")
	opt = input()
	
	if(opt == str(1)): # Send audio file to server1
		print("\nType the name of the audio file you wish to transfer")
		fileName = input()
		if(Path(fileName).is_file()):
			f = open(fileName, 'rb')
			w = open("output.txt", 'w')					# Testing
			
			fileLen = stat(fileName).st_size
			w.write(str(fileLen) + '\n')				# Testing
			
			clientSocket1.send(str(fileLen))			# Not working
			clientSocket1.send(fileName)
			
			while(1):
				toSend = f.read(1024)
				w.write(str(toSend))					# Testing
				clientSocket1.send(toSend)
				if(toSend == b''):
					print("Done sending\n")
					break
		else:
			print("File not found\n")
		
	elif(opt == str(2)): # Play an audio file with server2
		while(1):
			print("Type '1' to play an audio file")
			print("Type '2' to stop playing an audio file")
			print("Type '3' to list available audio files")
			print("Type 'q' to quit")
			opt3 = input()
			
			
	
	elif(opt == 'q'):
		print("Exiting")
		exit(0)
	else:
		print("That is an invalid option")
		continue













