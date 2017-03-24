////////////////////////////////////////////////////////////////////////
// Name: Breven Hettinger
// Course: COSC 4653 - Advanced Networks
// Assignment: #5 - Min-Max in C
// File Name: hettinger_5_server.c
//
// Description: Computes the maximum and minimum of values sent from the
// client and returns those values.
////////////////////////////////////////////////////////////////////////

#include <socket.h>
#include <time.h>
#include <stdio.h>
#include <strings.h>
#include <sockio.h>

int main(int argc, char **argv) {
	int	sockfd;
	struct sockaddr_in	servaddr;

	if (argc != 2)
		err_quit("usage: hettinger_5_server <port number>");

	sockfd = Socket(AF_INET, SOCK_STREAM, 0);

	bzero(&servaddr, sizeof(servaddr));
	servaddr.sin_family = AF_INET;
	servaddr.sin_port = htons(SERV_PORT);
	Inet_pton(AF_INET, argv[1], &servaddr.sin_addr);

	Connect(sockfd, (SA *) &servaddr, sizeof(servaddr));

	str_cli(stdin, sockfd);		/* do it all */

	exit(0);
}


