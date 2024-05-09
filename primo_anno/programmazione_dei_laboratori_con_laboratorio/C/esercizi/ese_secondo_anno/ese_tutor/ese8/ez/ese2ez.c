#include <stdio.h>

int main() {
  int x = 3;
  int *y = &x;
  printf("valore = %d \nindirizzo = %p", *y, y);
}
