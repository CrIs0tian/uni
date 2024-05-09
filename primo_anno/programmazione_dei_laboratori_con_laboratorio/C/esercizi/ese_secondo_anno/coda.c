/*
Esercizio 3. Una coda è una struttura dati su cui sono definite le seguenti
operazioni:

    coda_new(): restituisce una coda vuota

    coda_in(q, e): inserisce nella cosa l'elemento e

    coda_get(q): restituisce l'elemento che è presente nella coda q da più
tempo.

    coda_del(q): elimina dalla coda q l'elemento più vecchio.

Si implementi nel linguaggio C la struttura dati coda contenente float facendo
in modo che le operazioni sopra descritte abbiano complessità temporale costante
nel caso peggiore.
*/
#include <stdio.h>
#include <stdlib.h>
struct nodo {
  float e;
  struct nodo *prec, *succ;
};
typedef struct nodo nodo;
struct coda {
  nodo *first;
  nodo *last;
  int n;
};

typedef struct coda coda;

coda coda_new();
coda coda_in(coda, float);
float coda_get(coda);
coda coda_del(coda);
void mostra_coda(coda);

int main(int n, char *args[]) {

  coda q = coda_new();
  int i;
  for (i = 0; i < 10; i++) {
    q = coda_in(q, i);
  }
  mostra_coda(q);
  float e = coda_get(q);
  printf("\n%.2f", e);

  q = coda_del(q);
  mostra_coda(q);
}

coda coda_new() {
  coda q = {NULL, NULL, 0};
  return q;
}

coda coda_in(coda q, float e) {
  nodo *n = malloc(sizeof(nodo));
  n->e = e;
  if (q.first == NULL) {
    q.first = n;
    q.last = n;

  } else {
    q.first->prec = n;
    n->succ = q.first;
    q.first = n;
  }
  return q;
}

float coda_get(coda q) { return q.last->e; }

coda coda_del(coda q) {
  nodo *n = q.last;
  q.last->prec->succ = NULL;
  q.last = q.last->prec;
  free(n);
  return q;
}
void mostra_coda(coda q) {
  nodo *x = q.first;
  while (x != NULL) {
    printf("%.2f ", x->e);
    x = x->succ;
  }
}
