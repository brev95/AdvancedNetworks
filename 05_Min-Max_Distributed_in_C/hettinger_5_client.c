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

#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <strings.h>

static inline unsigned int
min(unsigned int a, unsigned int b, unsigned int c);

static inline unsigned int
max(unsigned int a, unsigned int b, unsigned int c);

int main(int argc, char **argv) {
	srand(time(NULL));
	
	int sockfd[3];
	struct sockaddr_in servaddr1, servaddr2, servaddr3;
	int lenNums = atoi(argv[1]);
	int nums [lenNums];
	int port1 = atoi(argv[3]);
	int port2 = atoi(argv[5]);
	int port3 = atoi(argv[7]);
	int i = 0;
	int minimum, maximum;
	char msg1[2], msg2[2], msg3[2];

	if (argc != 8){
		printf("usage: hettinger_5_client <# Integers> <First IP Address> <First Port Number> <Second IP Address> <Second Port Number> <Third IP Address> <Third Port Number>\n");
		exit(1);
	}	
	
	if (lenNums < 3){
		printf("# Integers must be greater than 3\n");
		exit(1);
	}

	for(i = 0 ; i <= lenNums; i++){
		nums[i] = rand() % (10000 + 1 - 0) + 0;
		printf("%d\n", nums[i]);
	}

	sockfd[0] = socket(AF_INET, SOCK_STREAM, 0);
	sockfd[1] = socket(AF_INET, SOCK_STREAM, 0);
	sockfd[2] = socket(AF_INET, SOCK_STREAM, 0);

	// Server 1
	bzero(&servaddr1, sizeof(servaddr1));
	servaddr1.sin_family = AF_INET;
	servaddr1.sin_port = port1;
	inet_pton(AF_INET, argv[2], &servaddr1.sin_addr);
	
	// Server 2
	bzero(&servaddr2, sizeof(servaddr2));
	servaddr2.sin_family = AF_INET;
	servaddr2.sin_port = port2;
	inet_pton(AF_INET, argv[4], &servaddr2.sin_addr);
	
	// Server 3
	bzero(&servaddr3, sizeof(servaddr3));
	servaddr3.sin_family = AF_INET;
	servaddr3.sin_port = port3;
	inet_pton(AF_INET, argv[6], &servaddr3.sin_addr);

	connect(sockfd[0], (struct sockaddr *) &servaddr1, sizeof(servaddr1));
	connect(sockfd[1], (struct sockaddr *) &servaddr2, sizeof(servaddr2));
	connect(sockfd[2], (struct sockaddr *) &servaddr3, sizeof(servaddr3));

	for(i = 0 ; i <= lenNums; i++){
		if(i % 3 == 1){
			send(sockfd[0], &nums[i], sizeof(int), 0);
		}
		else if(i % 3 == 2){
			send(sockfd[1], &nums[i], sizeof(int), 0);
		}
		else if(i % 3 == 0){
			send(sockfd[2], &nums[i], sizeof(int), 0);
		}
		sleep(0.05);
	}
	
	// Send -1 and parse received data
	send(sockfd[0], "-1", sizeof("-1"), 0);
	recv(sockfd[0], &msg1, sizeof(msg1) , 0);
	sleep(0.05);

	send(sockfd[1], "-1", sizeof("-1"), 0);
	recv(sockfd[1], &msg2, sizeof(msg2) , 0);
	sleep(0.05);

	send(sockfd[2], "-1", sizeof("-1"), 0);
	recv(sockfd[2], &msg3, sizeof(msg3) , 0);
	sleep(0.05);

	shutdown(sockfd[0], 2);
	shutdown(sockfd[1], 2);
	shutdown(sockfd[2], 2);

	// Get min
	minimum = min(msg1[0], msg2[0], msg3[0]);
	printf("Server minimum: %d\n", minimum);
	// Get max
	maximum = max(msg1[1], msg2[1], msg3[1]);
	printf("Server maximum: %d\n", maximum);
	
	
	minimum = 1000000;
	for(i = 0; i < lenNums; i++){
		if(nums[i] < minimum){
			minimum = nums[i];
		}
	}
	printf("Client minimum: %d\n", minimum);
	
	maximum = 0;
	for(i = 0; i < lenNums; i++){
		if(nums[i] > maximum){
			maximum = nums[i];
		}
	}
	
	printf("Client maximum: %d\n", maximum);

	exit(0);
}

static inline unsigned int
min(unsigned int a, unsigned int b, unsigned int c)
{
    unsigned int m = a;
    if (m > b) m = b;
    if (m > c) m = c;
    return m;
}

static inline unsigned int
max(unsigned int a, unsigned int b, unsigned int c)
{
    unsigned int m = a;
    if (m < b) m = b;
    if (m < c) m = c;
    return m;
}
