/* Esercizio. Implementare le funzioni
 * lista_out0(nodo *x) e
 * lista_out(nodo *x, int pos)
 * che, rispettivamente, cancellano
 * da una lista il nodo in posizione
 * 0 e quello in posizione pos.*/

#include <stdio.h>
#include <stdlib.h>

struct nodo {
  float info;
  struct nodo *prec, *succ;
};
typedef struct nodo nodo;

nodo *lista_vuota();
nodo *lista_in0(nodo *, float);
nodo *lista_in1(nodo *, float);
void lista_mostra(nodo *);
nodo *lista_cerca(nodo *, int);
nodo *lista_in(nodo *, int, float);
nodo *lista_out1(nodo *);
nodo *lista_out0(nodo *x);
nodo *lista_out(nodo *x, int pos);

int main() {

  nodo *p, *a = lista_vuota();

  a = lista_in0(a, 3.14);
  a = lista_in0(a, 2.71);
  a = lista_in0(a, 1.4);
  a = lista_in1(a, 2);
  lista_mostra(a);
  p = lista_cerca(a, 4);
  if (p != NULL)
    printf("%f\n", p->info);
  a = lista_in(a, 2, -1);
  a = lista_in(a, 0, 0);
  a = lista_in(a, 6, 6);
  lista_mostra(a);
  a = lista_out1(a);
  lista_mostra(a);
  a = lista_out0(a);
  a = lista_out(a, 3);
  lista_mostra(a);
}

nodo *lista_vuota() { return NULL; }

void lista_mostra(nodo *x) {
  nodo *p = x;

  while (p != NULL) {
    printf("%.2f ", p->info);
    p = (*p).succ;
  }
  printf("\n");
}

nodo *lista_in0(nodo *x, float e) {
  nodo *n = malloc(sizeof(nodo));

  n->info = e; // equivale a (*n).info
  (*n).succ = x;
  n->prec = NULL;
  if (x != NULL) // se lista non vuota
    (*x).prec = n;

  return n;
}

nodo *lista_in1(nodo *x, float e) {
  nodo *n, *p;

  if (x == NULL)
    return NULL;

  p = x->succ;

  n = malloc(sizeof(nodo));

  n->info = e;
  n->prec = x;
  n->succ = p;

  x->succ = n;
  if (p != NULL)
    p->prec = n;

  return x;
}

nodo *lista_cerca(nodo *x, int pos) {
  /*
   * ritorna il puntatore al nodo in posizione pos di x.
   * Se tale nodo non esiste, la funzione ritorna NULL.
   *
   */
  nodo *p = x;
  int c = 0;

  while (p != NULL && c != pos) {
    p = p->succ;
    c++;
  }

  return p;
}

nodo *lista_in(nodo *x, int pos, float e) {
  nodo *p;

  if (pos == 0)
    return lista_in0(x, e);

  p = lista_cerca(x, pos - 1);

  if (p == NULL)
    return x;

  p = lista_in1(p, e);
  return x;
}

nodo *lista_out1(nodo *x) {
  nodo *t;

  if (x == NULL || x->succ == NULL)
    return x;

  t = x->succ;

  x->succ = t->succ;
  if (t->succ != NULL)
    t->succ->prec = x;

  free(t);

  return x;
}

nodo *lista_out0(nodo *x) {
  if ((x->succ) == NULL || x == NULL) {
    free(x);
    nodo *x = lista_vuota();
  } else {
    nodo *a = x->succ;
    a->prec = NULL;
    x->succ = NULL;
    free(x);
    return a;
  }
}

nodo *lista_out(nodo *x, int pos) {
  if (pos == 0) {
    x = lista_out0(x);
  }
  nodo *t = lista_cerca(x, pos - 1);

  t = lista_out1(t);
  return x;
}
