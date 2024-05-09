
/*
Esercizio Si scriva un programma che ordini in modo
lessicografico le stringhe passate alla linea di comando.
Come algoritmo di ordinamento si utilizzi il Bubble-sort.

usando strcmp, una funzione ch econfronta due stringhe ( costo tempo
O(min(len(n), len(m)))) e restituisce un numero che : -se maggiore di 0, prima
stringa > seconda stringa -se = 0, stringhe uguali -se <0, sseconda stringa >
prima stringa
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void bubble_sort(char **, int);

int main(int n, char *args[]) {
  bubble_sort(args + 1, n - 1);
  int i;
  for (i = 0; i < n; i++) {
    printf("%s\n", args[i]);
  }
}

void bubble_sort(char *t[], int n) {
  char *a;
  int i, ordinato = 0, c = 0;
  while (ordinato == 0) {
    ordinato = 1;
    for (i = 0; i < n - 1 - c; i++) {
      if (strcmp(t[i], t[i + 1]) > 0) {
        ordinato = 0;
        a = t[i];
        t[i] = t[i + 1];
        t[i + 1] = a;
      }
    }
    c++;
  }
}
