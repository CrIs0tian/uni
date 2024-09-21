#include <stdio.h>
#include <stdlib.h>

float *linspace(float, float, int);
int main(int num, char **argv) {
  float *m;
  m = linspace(2.0, 5.3, 7);
}

float *linspace(float from, float to, int num) {
  float *m = malloc(num * sizeof(float));
  float step = (to - from) / (num - 1);
  int i = 0;
  while (i <= num) {
    m[i] = from + (i * step);
    i++;
  }
  for (int l = 0; l < num; l++) {
    printf("%f ", m[l]);
  }
  return m;
}
