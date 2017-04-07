////////////////////////////////////////////////////////////////////////
// Name: Breven Hettinger
// Course: COSC 4653 - Advanced Networks
// Assignment: #6 - Robust TCP Client/Server
// File Name: hettinger_5_server.c
//
// Description: 
////////////////////////////////////////////////////////////////////////

#include <protocol-records.h>
#include <socket.h>
#include <time.h>
#include <stdio.h>
#include <strings.h>
#include <sockio.h>

#define QUERYSIZE (sizeof(queryRecordType))
#define RESPSIZE (sizeof(responseRecordType))

typedef struct
	{
		int ID;
		int Sector; 
	} databaseServer;


void argCheck(int argc);
void setupDatabase();
void setupSignals();
void sigChildHandler(int signo);
void sigPipeHandler(int signo);
void sigTermHandler(int signo);
int handleConn(int fd);
void readQuery(int fd, queryRecordType &rec);
void handleErr(char* str);
void bufToQueryRec(char buf, queryRecordType &rec);
void getIdBySector(char text[], responseRecordType rsp);
void getSectorById(char text[], responseRecordType rsp);

int main(int argc, char** argv){
	
argCheck(argc);

setupDatabase();

databaseRecordType database [20];

setupSignals();




}

void argCheck(int argc){
	if(argc != 2){
		printf("usage: ./hettinger_6_server <portNum>\n");
		exit(1);
	}
	return;
}

void setupDatabase(){
	strncpy(database[0].ID, "1234", MAX_ID_TEXT);
	//...
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

void sigChildHandler(int signo){
	pid_t	pid;
	int		stat;

	while((pid = waitpid(-1, &stat, WNOHANG)) > 0){
		printf("child %d terminated\n", pid);
	}
	return;
}

void sigPipeHandler(int signo){
	printf("The connection has been broken");
	close(sockfd);
	return;
}

void sigTermHandler(int signo){
	pid_t	pid;
	printf("The process %d terminated\n", pid);
	return;
}

int handleConn(int fd){
	char buf[QUERYSIZE];
	char outBuf[RESPSIZE];
	queryRecordType rec;
	responseRecordType outRec;
	
	readQuery(fd, &rec);

	outRec.command = rec.command;
	switch(rec.command){
		case 0:
			getTimeStr(outRec.data.text, MAX_MESSAGE_TEXT);
			break;
		case 1:
			getSectorById(rec.text, outRec.data);
			break;
		case 2:
			getIdBySector(rec.text, outRec.data);
			break;
		default:
			break;
	}
	
	// Missing stuff here
	
	return 0;
}

void readQuery(int fd, queryRecordType &rec){
	int nbytes = read(fd, buf, QUERYSIZE);
	if(nbytes < 0){
		if(errno == EINTR{
			continue;
		} else {
			handleErr("Read Error");
		}
	}
	else if(nbytes == 0){
		printf("Client send EOF");
		return -1;
	}
	bufToQueryRec(buf, &rec);
}

void handleErr(char* str){
	perror(str);
	fflush(STDERR);
	exit(1);
}

void bufToQueryRec(char buf, queryRecordType rec){
	
}

void getTimeStr(outRec.data.text){ // fix parameters
	time_t ticks;
	ticks = time(NULL);
	strncpy(outRec.data.text, (ctime(ticks)), MAX_MESSAGE_TEXT);
}

void getIdBySector(char text[], responseRecordType rsp){
	int i;
	for(i = 0; i < 10, i++){
		if(strcmp(database[i].sector, text) == 0){
			resp.status = '1';
			strncpy(resp.data.record.ID, database[i].ID, MAX_ID_TEXT);
			strncpy(resp.data.record.sector, database[i].sector, MAX_SECTOR_TEXT);
			return;
		}
	}
	resp.status = 0;
	strncpy(resp.data.text, "Record not found", MAX_MESSAGE_TEXT);
	return;
}

void getSectorById(){
	
}

void readQuery(int fd, queryRecordType rec){
	while(){
		
	}
}
