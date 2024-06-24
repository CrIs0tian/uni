#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *str_cat(char *, int, char *);
char *mod(char *);
int main(int n, char *args[]) {
  char *a = malloc(9 * sizeof(char));
  char *b = malloc(9 * sizeof(char));
  for (int i = 0; i < 8; i++) {
    a[i] = 'o';
    b[i] = 'o';
  }
  b[8] = '\0';
  b[8] = '\0';
  printf("%s\n%s\n", a, b);
  int j = 8;
  a = str_cat(a, j, b);
  printf("%s", a);
}

char *str_cat(char *a, int n, char *b) {
  int len_a = strlen(a);
  int len_b = strlen(b);
  if (n < len_a + len_b + 1) {
    n = len_b + len_a + 1;
    a = realloc(a, n * sizeof(char));
  }
  for (int i = 0; i < len_b; i++) {
    a[len_a + i] = b[i];
  }
  a[n - 1] = '\0';
  free(b);

  return a;
}
/*
 * len  a =n
 * len b = m
 * costo temporale = O(n+m) nel caso peggiore,se bisogna fare il realloc, O(m)
 * nel caso migliore,
 *
 * costo spaziale = O(1)*/
