///////////////////////////////////////////////////////////////////
// Student name: Instructor
// Course: COSC 4653 - Advanced Networks
// Assignment: Demonstration
// File name: home-and-foreign-addresses.c
// Purpose: Prints the local and foreign IP addresses
//
// Limitations: 
// Development Computer: HP dv4
// Operating System: Windows 7
// Integrated Development Environment (IDE): wordpad
// Compiler: gcc (CYGWIN)
// Operational Status: Meets all requirements
///////////////////////////////////////////////////////////////////

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

// Prototypes
int makeServerSocket(int port);
int handleClient(int clientfd);

// ################################################################
int main(int argc, char *argv[])
   {
   int status;
   int listenfd;
   int clientfd;
   struct sockaddr_in clientAddress;
   struct sockaddr_in serverAddress;
   int length;
   char buffer[INET_ADDRSTRLEN];

   if(argc != 2)
      {
      fprintf(stderr, "Usage: %s <port number> \n", argv[0]);
      exit(0);
	} // End if   
	
   listenfd = makeServerSocket(atoi(argv[1]));
   if (listenfd < 0)
      {
      exit(1);
      } // End if

   while(1)
      {
      clientfd = accept(listenfd, (struct sockaddr *) NULL, NULL);
      if (clientfd < 0)
         {
         perror("Server: accept");
         } // End if
		
      getsockname(listenfd, (struct sockaddr *) &serverAddress, &length);
      inet_ntop(AF_INET, &serverAddress.sin_addr, buffer, sizeof(buffer)); 

      printf("(Local Node) IP Address: %s, Port: %d\n",
      buffer, ntohs(serverAddress.sin_port));

      getpeername(clientfd, (struct sockaddr *) &clientAddress, &length);
      inet_ntop(AF_INET, &clientAddress.sin_addr, buffer, sizeof(buffer)); 

      printf("(Foreign Node) IP Address: %s, Port: %d\n",
      buffer, ntohs(clientAddress.sin_port));

      status = handleClient(clientfd);
      if (status < 0)
         break;
		
	} // End while
	
   close(listenfd);

   exit(0);
} // End main



//##########################################################################
int makeServerSocket(int port)
{
int status;
int listenfd;
struct sockaddr_in serverAddress;
	
listenfd = socket(AF_INET, SOCK_STREAM, 0);
if (listen < 0)
   {
   perror("Server: socket");
   return 1;
   } // End if

bzero(&serverAddress, sizeof(serverAddress));
serverAddress.sin_family      = AF_INET;
serverAddress.sin_addr.s_addr = htonl(INADDR_ANY);
serverAddress.sin_port        = htons(port);

status = bind(listenfd, (struct sockaddr *) &serverAddress, sizeof(serverAddress));
if (status < 0)
   {
   perror("Server: bind");
   return 1;
   } // End if

status = listen(listenfd, MAX_LISTEN_QUEUE_LENGTH);
if (status < 0)
   {
   perror("Server: listen");
   return 1;
   } // End if
	
return listenfd;

} // End makeServerSocket



//##########################################################################
int handleClient(int clientfd)
{
int status;
char buffer[MAX_LINE_LENGTH];
ssize_t dataSize;
	
dataSize = read(clientfd, buffer, MAX_LINE_LENGTH);

printf("Client sent this: %*s\n", dataSize, buffer);		

	
snprintf(buffer, MAX_LINE_LENGTH, "%d %d", min, max);
status = write(clientfd, buffer, strlen(buffer));
if (status < strlen(buffer))
   {
   perror("Server: error writing to client");
   } // End if
   
close(clientfd);
return 0;
} // End handleClient
