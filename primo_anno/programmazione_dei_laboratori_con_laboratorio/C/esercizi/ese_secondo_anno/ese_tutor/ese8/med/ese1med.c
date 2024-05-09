#include <stdio.h>

void aumenta(float *, int);
int main() {
  float pi = 3.14;

  aumenta(&pi, 1);

  printf("%f\n", pi);
}
void aumenta(float *e, int v) { *e += v; }
