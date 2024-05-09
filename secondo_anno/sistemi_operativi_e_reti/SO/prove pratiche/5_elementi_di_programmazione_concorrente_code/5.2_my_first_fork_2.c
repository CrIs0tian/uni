#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define STDIN 0
#define STDOUT 1
#define PIPE_RD 0
#define PIPE_WR 1

void main(void) {
  int pid, child_status;
  char *args[] = {"/bin/ls", "-l", NULL};
  if ((pid = fork()) == 0) {
    execv(args[0], args);
  } else {

    wait(&child_status);
    printf("%s", args[0]);
  }
}
