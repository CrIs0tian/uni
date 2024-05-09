#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#define STDIN 0
#define STDOUT 1
#define PIPE_RD 0
#define PIPE_WR 1
int main() {
  int pid1, pid2, somma, n, n1;
  int fd1[2], fd2[2];

  pipe(fd1);
  pipe(fd2);
  pid1 = fork();
  if (pid1 == 0) {
    close(fd1[PIPE_RD]);
    close(STDOUT);

    while (1) {
      n = rand() % 101;
      if ((n % 2) == 1) {
        dup(fd1[PIPE_WR]);
        write(fd1[PIPE_WR], &n, sizeof(n));
      }
    }
  } else if (pid1 != 0) {
    pid2 = fork();
    if (pid2 == 0) {
      close(fd2[PIPE_RD]);
      close(STDOUT);
      while (1) {
        n = rand() % 101;
        if ((n % 2) == 0) {
          dup(fd2[PIPE_WR]);
          write(fd2[PIPE_WR], &n, sizeof(n));
        }
      }
    } else if (pid2 != 0) {
      close(fd1[PIPE_WR]);
      close(fd2[PIPE_WR]);

      while (1) {
        read(fd1[PIPE_RD], &n, sizeof(n));
        read(fd2[PIPE_RD], &n1, sizeof(n1));
        somma = n + n1;
        printf("n1=%d, n2=%d, somma=%d \n", n, n1, somma);
        if (somma > 190) {
          printf("MA CHE OHHHH\n");
          kill(pid1, SIGKILL);
          kill(pid2, SIGKILL);
          return 0;
        }
      }
    }
  }
}
