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
  int pid1, pid2;
  int fd1[2], fd2[2];
  pipe(fd1);
  pid1 = fork();
  if (pid1 == 0) {
    close(fd1[PIPE_RD]);
    close(STDOUT);

    while (1) {
      int n = rand() % 101;
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
        int n = rand() % 101;
        if ((n % 2) == 0) {
          dup(fd2[PIPE_WR]);
          write(fd2[PIPE_WR], &n, sizeof(n));
        }
      }
    }
  }
}
