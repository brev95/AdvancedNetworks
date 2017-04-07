////////////////////////////////////////////////////////////////////////
// Name: Breven Hettinger
// Course: COSC 4653 - Advanced Networks
// Assignment: #6 - Robust TCP Client/Server
// File Name: hettinger_5_server.c
//
// Description: 
////////////////////////////////////////////////////////////////////////

// kill -s ____ pid		send signal
// kill -l 				kill types

//#include <protocol-records.h>
#include <sys/socket.h>
#include <time.h>
#include <stdio.h>
#include <strings.h>
#include <sockio.h>

void argCheck(int argc);
void setupSignals();
void printMenu();

int main(int argc, char** argv){
	
	argCheck(argc);

	setupSignals();

	checkIP(); // convert IP inet.pton()

	makeConn(); // make socket, sd = connect

	handleConn();

	return 0;
}

void argCheck(int argc){
	if(argc != 3){
		printf("usage: ./hettinger_6_client <ip address> <portNum>\n");
		exit(1);
	}
	return;
}

void setupSignals(){
	struct sigaction newSig, oldSig;
	newSig.sa_handler = sigChildHandler;
	newSig.sa_handler = sigPipeHandler;
	newSig.sa_handler = sigTermHandler;
	
	sigaction(SIGCHLD, &newSig, &oldSig);
	sigaction(SIGPIPE, &newSig, &oldSig);
	sigaction(SIG, &newSig, &oldSig);
}

int handleConn(){
	
	printMenu();

	
	while(1){
		// setup select
		FD_SET(fileno(stdin), &fds);
		FD_SET(sd, &fds);
		
		// select
		result = select(maxfdp1, &fds, NULL, NULL, NULL);
		
		
		if(FD_ISSET(fileno(stdin), &fds)){
			switch(){
				case 0:
					
					break;
				case 1:
				
					break;
				case 2:
				
					break;
				case 3:
					printf("Thank you :) Have a good day.\n");
					exit(1);
					break;
				default:
					printf("Not a valid option.\n");
					exit(-1);
					break;
			}
		}
		
		if(FD_ISSET(sd, &fds)){
			
			printMenu();
		}
		// if FD_SET
			// stdin
				// handleUserSelection()
				
			// sd
				// readResponse()
				// print response
	}
}

void printMenu(){
	printf("\n*************************************\n");
	printf("* 0 - Make a Current Date/Time query\n");
	printf("* 1 - Make an ID query\n");
	printf("* 2 - Make a sector query\n");
	printf("* 3 - End the client process\n");
	printf("***************************************\n");
}
