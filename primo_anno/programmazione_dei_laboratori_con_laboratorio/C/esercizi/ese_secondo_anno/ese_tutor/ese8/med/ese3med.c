#include <stdio.h>
#include <stdlib.h>

// scrivi qui la funzione array_di_uno
int *array_di_uno(int *, int);
int main() {
  // definisco gli array
  int a[3] = {1, 2, 8};
  int *b = NULL;

  // chiamo la funzione array di uno che dovete programmare voi
  b = array_di_uno(a, 3);
  // stampo l'array di uni
}

int *array_di_uno(int *a, int n) {
  int i, sum = 0;
  int *b;
  for (i = 0; i < n; i++) {
    sum += a[i];
  }
  b = malloc(sum * sizeof(int));
  printf("%d", sizeof(b));
  for (i = 0; i < sum; i++) {
    b[i] = 1;
  }
  printf("Array di uni:[ "); // queste sono solo lì per bellezza
  for (int i = 0; i < sum; i++) {
    printf("%d,", b[i]); // stampa l'i esimo elemento dell'array di uni
  }
  printf("]\n"); // queste sono solo lì per bellezzai
}
