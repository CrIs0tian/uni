#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *get_format(char *);
int main() {

  char a[] = "883;90;0645456;124;864;466";
  char *b = &a;
  b = get_format(b);
  printf("%s", b);
}

char *get_format(char *a) {
  int n = strlen(a);
  int i = 0, j = 0, k;
  while (a[j] != '\0') {
    if (a[j] != ';') {
      while (a[j + 1] != ';' && a[j + 1] != '\0') {
        j++;
      }
      sscanf(&a[j], "%d", &k);
      if (k % 2 == 0) {
        a[i] = 'p';
      } else {
        a[i] = 'd';
      }
      i++;
      j++;

    } else {
      a[i] = ';';
      i++;
      j++;
    }
  }
  a[i] = '\0';

  return a;
}
// csoto temporale = O(n)  n = len(a)
