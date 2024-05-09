#include <stdio.h>
// le liste in c si chiamano array, cioè vettori ci char, molto importante!
// costo computazionale di lettura e scrittura in un array = tempo costante,
// poichè ogni elemento è lo stesso tipo (stesso sapazio occupato in memoria)
// (per quanto riguarda l'INDICIZAZZIONE cioè si sa la posizione dell'elemento
// nell'array) e un array richiamato in una funzione contiene solo due
// informazioni, il tipo di dati
// contenuto nell'array e l'INDIRIZZO del primo byte che contiene il primo
// elemento dell'array

void change_array(int x[], int n) {
  int i;
  for (i = 0; i < n; i++) {
    x[i] = 10 * i;
  }
}

int main() {
  int a[10];
  int b[] = {0, 10, 20, 30,
             40}; // quindi qua dentro se lo richiamiamo come b, stiamo
                  // richiamando il suo indirizzo non l'array stesso
  int c[5] = {0, 10, 20, 30, 40};
  int d[15] = {0, 10, 20, 30, 40};
  int e[100] = {0};
  int i, len_d;

  d[11] = 21;
  printf("%d, %d, %d, %d, %d, %d\n", a[4], b[0], c[2], d[10], e[97], d[11]);

  len_d = sizeof(d) / sizeof(int);

  printf("------ %d\n", len_d);
  // fare attenzione della lunghezza degli array, il compilatore non blocca
  // eventauli indici che vanno oltre la lunghezza di un array, e in run time
  // scrive cose a cazzum
  for (i = 0; i < len_d; i++) {
    printf("%d\n", d[i]);
  }

  change_array(d, len_d);
  for (i = 0; i < len_d; i++) {
    printf("%d\n", d[i]);
  }
}
