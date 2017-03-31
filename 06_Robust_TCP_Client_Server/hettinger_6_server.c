////////////////////////////////////////////////////////////////////////
// Name: Breven Hettinger
// Course: COSC 4653 - Advanced Networks
// Assignment: #6 - Robust TCP Client/Server
// File Name: hettinger_5_server.c
//
// Description: 
////////////////////////////////////////////////////////////////////////

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


int main(int argc, char** argv){
	
argCheck(argc);

setupDatabase();

databaseRecordType database [20];

setupSignals();




}

void argCheck(int argc){
	if(argc != 2){
		printf("usage: hettinger_6_server <portNum>\n");
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

