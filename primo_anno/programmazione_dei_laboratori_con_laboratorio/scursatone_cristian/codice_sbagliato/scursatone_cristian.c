#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *get_format(char *);
int main() {

  char a[] = "7;90;0;123;8;4";
  char *b = &a;
  b = get_format(b);
  printf("%s", b);
}

char *get_format(char *a) {
  int n = strlen(a);
  char *c = malloc(n * sizeof(char) + 1);
  for (int i = 0; i < n; i++) {
    c[i] = a[i];
    a[i] = '0';
  }
  c[n] = '\0';
  int i = 0, j = 0, k;
  while (c[i] != '\0') {
    if (c[i] != ';') {
      while (c[i + 1] != ';' && c[i + 1] != '\0') {
        i++;
      }
      sscanf(&c[i], "%d", &k);
      if (k % 2 == 0) {
        a[j] = 'p';
      } else {
        a[j] = 'd';
      }
      j++;
      i++;
    } else {
      a[j] = ';';
      j++;
      i++;
    }
    a[j] = '\0';
  }
  free(c);
  return a;
}

// costo spaziale = O(1)
// csoto temporale = O(n)  n = len(a)
