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
from time import *
import cPickle as pickle
import numpy

# Check for usage error
if len(argv) != 4:
	print "usage: python hettingerSS.py <Port Number> <Maximum Table Size> <Maximum Aging Time>"
	quit()

# Variables
port = int(argv[1])
maxTableSize = int(argv[2])
maxAgingTime = int(argv[3])
table = [maxTableSize][2]

# Set up socket
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(("", 6000))

