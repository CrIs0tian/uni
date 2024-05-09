#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define STDIN 0
#define STDOUT 1
#define PIPE_RD 0
#define PIPE_WR 1

int main() {

  int pid, child_status = 3;

  if ((pid = fork()) == 0) {
    printf("I am the child and I see the PID %d\n", pid);
    sleep(5);
    signal(SIGSTOP, SIG_DFL);
  }

  else {
    printf("%d", child_status); // qui è 3 ma dopo il wait diventa 0
    wait(&child_status); // aspetta che il figlio finisce o cambia stato (quindi
                         // può essere in ready o blocked, il padre scrive lo
                         // stato)
    printf("I am the parent, I see the child's PID (%d) and the statud (%d)\n",
           pid, child_status);
  }
}
