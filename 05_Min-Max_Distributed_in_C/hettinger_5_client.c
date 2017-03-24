////////////////////////////////////////////////////////////////////////
// Name: Breven Hettinger
// Course: COSC 4653 - Advanced Networks
// Assignment: #5 - Min-Max in C
// File Name: hettinger_5_client.c
//
// Description: Creates a list of randomly-generated positive integers,
// pass a third of the list to each of three servers, read the maximum
// and minimum returned by the server, and print the combined maximum
// and minimum.
////////////////////////////////////////////////////////////////////////

#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

#pragma comment(lib, "socket.lib")


int main(int argc, char **argv) {
	srand(time(NULL));
	
	int	sockfd;
	struct sockaddr_in servaddr1, servaddr2, servaddr3;
	int nums [atoi(argv[1])];
	int lenNums = atoi(argv[1]);
	int port1 = atoi(argv[3]);
	int port2 = atoi(argv[5]);
	int port3 = atoi(argv[7]);

	if (argc != 8)
		printf("usage: hettinger_5_client <# Integers> <First IP Address> <First Port Number> <Second IP Address> <Second Port Number> <Third IP Address> <Third Port Number>");
		exit(1);
		
	if (lenNums < 3){
		printf("# Integers must be greater than 3");
		exit(1);
	}

	int i = 0;
	for( ; i <= lenNums; i++){
		nums[i] = rand();
		printf("%d\n", nums[i]);
	}

	sockfd = Socket(AF_INET, SOCK_STREAM, 0);

	// Server 1
	bzero(&servaddr1, sizeof(servaddr1));
	servaddr1.sin_family = AF_INET;
	servaddr1.sin_port = port1;
	Inet_pton(AF_INET, argv[2], &servaddr1.sin_addr);
	
	// Server 2
	bzero(&servaddr2, sizeof(servaddr2));
	servaddr2.sin_family = AF_INET;
	servaddr2.sin_port = port2;
	Inet_pton(AF_INET, argv[4], &servaddr2.sin_addr);
	
	// Server 3
	bzero(&servaddr3, sizeof(servaddr3));
	servaddr3.sin_family = AF_INET;
	servaddr3.sin_port = port3;
	Inet_pton(AF_INET, argv[6], &servaddr3.sin_addr);

	Connect(sockfd, (struct sockaddr *) &servaddr1, sizeof(servaddr1));
	Connect(sockfd, (struct sockaddr *) &servaddr2, sizeof(servaddr2));
	Connect(sockfd, (struct sockaddr *) &servaddr3, sizeof(servaddr3));

	

	exit(0);
}

