#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void filtra(char *, int *);

void filtra(char *a, int *b) {
  int n = strlen(a);
  int i = 0;
  int j = 0;
  while (i < n) {
    if (b[i] == 1) {
      a[j] = a[i];
      j++;
    }
    i++;
  }
  a[j] = '\0';
}

int main() {
  char a[] = "algoritmo";
  int b[] = {0, 0, 0, 0, 0, 0, 1, 0, 1};
  filtra(a, b);
  printf("a = %s", a);
}
