// Demonstrates how to print out the IP addresses and port
// numbers of the client and server nodes

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

// ####################################################
int main(int argc, char *argv[]){
   int status;
   int listenfd;
   int clientfd;
   struct sockaddr_in clientAddress;
   struct sockaddr_in serverAddress;
   int length;
   char buffer[INET_ADDRSTRLEN];
	
   if (argc != 2){
      fprintf(stderr, "Usage: %s <port number> \n", argv[0]);
      exit(0);
      }//End if 
	
   listenfd = makeServerSocket(atoi(argv[1]));
   if(listenfd < 0){
      exit(1);
   }// End if

   while(1){
      clientfd = accept(listenfd, (struct sockaddr *) NULL, NULL);
      if(clientfd < 0){
         perror("Server: accept");
      }// End if
		
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

      }// End while
	
   close(listenfd);
   return 0; 
} // End main
