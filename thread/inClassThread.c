#include <pthread.h>

void *printThread(void *arg){
	int *n = (int*) arg;
	printf("%d\n", *n);
	while(1){}
}

int main(int argc, char** argv){
	int count = atoi(argv[1]);
	pthread_t s[count];
	pthread_t thread_t;
	int i = 0;
	int threadCount[count];
	
	for( ; i < count; i++){
		threadCount[i] = i;
		pthread_create(&s[i], NULL, printThread, &threadCount[i]);
	}
	
	i = 0;
	for( ; i < count; i++){
		pthread_join(s[i], NULL);
	}
}
