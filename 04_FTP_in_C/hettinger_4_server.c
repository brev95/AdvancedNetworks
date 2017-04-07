////////////////////////////////////////////////////////////////////////
// Name: Breven Hettinger
// Course: COSC 4653 - Advanced Networks
// Assignment: #4 - FTP in C
// File Name: hettinger_4_server.c
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
#include	<sys/uio.h>     // for iovec{} and readv/writev 
#include	<unistd.h>
#include	<sys/wait.h>
#include	<sys/un.h>		// for Unix domain sockets 

#define	MAX_LINE_LENGTH	256	      // max text line length 
#define	MAX_LISTEN_QUEUE_LENGTH 10	// 2nd argument to listen() 


// ################################################################
int main(int argc, char **argv)
{
int status;
int listenfd;
int clientfd;
struct sockaddr_in serverAddress;
char buffer[MAX_LINE_LENGTH];
time_t clockTicks;

listenfd = socket(AF_INET, SOCK_STREAM, 0);

bzero(&serverAddress, sizeof(serverAddress));
serverAddress.sin_family      = AF_INET;
serverAddress.sin_addr.s_addr = htonl(INADDR_ANY);
serverAddress.sin_port        = htons(21);	/* ftp port */

bind(listenfd, (struct sockaddr *) &serverAddress, sizeof(serverAddress));

listen(listenfd, MAX_LISTEN_QUEUE_LENGTH);

// Infinite loop
for ( ; ; ) 
   {
   clientfd = accept(listenfd, (struct sockaddr *) NULL, NULL);

   clockTicks = time(NULL);
   snprintf(buffer, sizeof(buffer), "%.24s\r\n", ctime(&clockTicks));
   write(clientfd, buffer, strlen(buffer));

   close(clientfd);
   } // End for

return 0;
} // End main
