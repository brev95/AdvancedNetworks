////////////////////////////////////////////////////////////////////////
// Name: Breven Hettinger
// Course: COSC 4653 - Advanced Networks
// Assignment: #4 - FTP in C
// File Name: hettinger_4_client.c
//
// Description: 
////////////////////////////////////////////////////////////////////////

#include	<sys/types.h>	// basic system data types 
#include	<sys/socket.h>	// basic socket definitions 
#include	<sys/time.h>	// timeval{} for select() 
#include	<netinet/in.h>	// sockaddr_in{} and other Internet defns 
#include	<arpa/inet.h>	// inet(3) functions 
#include	<errno.h>
#include	<fcntl.h>		// for nonblocking 
#include	<netdb.h>
#include	<signal.h>
#include	<stdio.h>
#include	<stdlib.h>
#include	<string.h>
#include	<sys/stat.h>	// for S_xxx file mode constants 
#include	<sys/uio.h>	// for iovec{} and readv/writev 
#include	<unistd.h>
#include	<sys/wait.h>
#include	<sys/un.h>		// for Unix domain sockets 

#define	MAX_LINE_LENGTH	256	// max text line length 
#define	SA	struct sockaddr


// #################################################
int main(int argc, char **argv)
{
int status;
int	 socketfd;
int    nbrBytesRead;
char	 receiveLine[MAX_LINE_LENGTH + 1];
struct sockaddr_in	serverAddress;

if (argc != 2)
   {
   fprintf(stderr, "Usage: a.out <IP address>");
   exit(1);
   } // End if        

socketfd = socket(AF_INET, SOCK_STREAM, 0);  

bzero(&serverAddress, sizeof(serverAddress));
serverAddress.sin_family = AF_INET;
serverAddress.sin_port   = htons(21);	 // ftp port

inet_pton(AF_INET, argv[1], &serverAddress.sin_addr);

connect(socketfd, (SA *) &serverAddress, sizeof(serverAddress));

nbrBytesRead = read(socketfd, receiveLine, MAX_LINE_LENGTH);

while (nbrBytesRead > 0) 
   {
   receiveLine[nbrBytesRead] = 0;	// null byte 
   fputs(receiveLine, stdout);
   nbrBytesRead = read(socketfd, receiveLine, MAX_LINE_LENGTH);
   } // End while

return 0;
} // End main
