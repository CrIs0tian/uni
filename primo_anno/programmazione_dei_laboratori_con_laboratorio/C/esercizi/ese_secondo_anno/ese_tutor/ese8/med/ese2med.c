#include <stdio.h>

int main() {
  int a[3] = {1, 2, 3};
  int *b = a;
  int i;
  for (i = 0; i < 3; i++) {
    printf("%d\n", *(b + i));
  }
}
