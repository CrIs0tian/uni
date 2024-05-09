#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <time.h>
#define STDIN 0
#define STDOUT 1
#define PIPE_RD 0
#define PIPE_WR 1 
int main (){
    int fd[2]; 
    int pid,pid1, child_s;
    pipe(fd);
    pid = fork();
    if (pid==0){
    	int n = 20;
    	close(fd[PIPE_RD]);
    	close(STDOUT);
    	dup(fd[PIPE_WR]);
    	write(fd[PIPE_WR],&n, sizeof(int));
    } else if (pid != 0){
    close(fd[PIPE_WR]);
    close(STDIN);
    dup(fd[PIPE_RD]);
    int i;
    int k;
    k=read(fd[PIPE_RD], &i, sizeof(int));
    printf("%d", i);
    }
    
}
    
    
    
    
   
    
    

    
    
    

