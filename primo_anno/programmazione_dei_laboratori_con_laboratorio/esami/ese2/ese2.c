
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void remove_non_alpha(char *);

void main() {

  char a[] = "pyt;on";
  char *p;
  p = a;
  remove_non_alpha(p);
}

void remove_non_alpha(char *a) {
  int len_a = strlen(a);
  int i = 0;
  int j = 0;
  while (i != len_a) {
    if ((a[i] >= 'A' && a[i] <= 'Z') || (a[i] <= 'z' && a[i] >= 'a')) {
      a[j] = a[i];
      j++;
    }
    i++;
  }
  a[j] = '\0';
  printf(a);
}
