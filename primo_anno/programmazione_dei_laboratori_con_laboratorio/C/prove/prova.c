#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  char *a = "3";
  int i = 0, n = 0;

  while (a[i] != '\0') {
    n += a[i];
    i++;
  }
  printf("%d", n);
}
