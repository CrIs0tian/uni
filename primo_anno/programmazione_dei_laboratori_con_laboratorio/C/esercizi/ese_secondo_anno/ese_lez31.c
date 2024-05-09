/*
  Esercizio 1 Scrivere una funzione avente il seguente prototipo:

  nodo *lista_cerca(nodo *x, int pos);

  La funzione prenda in input una lista x ed un intero pos e
  ritorni il puntatore al nodo in posizione pos di x.
  Se tale nodo non esiste, la funzione ritorni NULL.




  Esercizio 2 Scrivere una funzione avente il seguente prototipo:

  nodo *lista_in(nodo *x, int pos, float e);

  La funzione prenda in input una lista x , un intero pos ed un float e ed
  inserisca un nuovo nodo contenente l'informazione e in posizione pos di x . La
  funzione ritorni la lista modificata oppure x nel caso la posizione pos non
  esista.

*/

#include <stdio.h>
#include <stdlib.h>

struct nodo {
  float info;
  struct nodo *prec, *succ;
};

typedef struct nodo nodo;
nodo *lista_cerca(nodo *, int);
nodo *lista_in(nodo *, int, float);
nodo *lista_vuota(); /* ritorna un puntatore a node vuoto*/
nodo *listain0(nodo *, float);
void mostra(nodo *);

int main(int n, char *args[]) {
  int i;
  nodo *a = lista_vuota();
  for (i = 0; i < 10; i++) {
    a = listain0(a, i);
  }
  mostra(a);
  nodo *b = lista_cerca(a, 12);
  if (b == NULL) {
    printf("NULL\n");
  } else {
    printf("%.2f", b->info);
  }
  a = lista_in(a, 1, 24);
  mostra(a);
}

nodo *lista_vuota() { return NULL; }

void mostra(nodo *x) {
  nodo *p = x;

  while (p != NULL) {
    printf("%.2f ", p->info);
    p = p->succ;
  }
  printf("\n");
}

nodo *listain0(nodo *a, float e) {
  nodo *n;
  n = malloc(sizeof(nodo));
  n->info = e;
  n->succ = a;
  n->prec = NULL;

  if (a != NULL) {
    a->prec = n;
  }
  return n;
}

nodo *lista_cerca(nodo *x, int pos) {
  nodo *n = x;
  while (n != NULL) {
    pos--;
    if (pos == 0) {
      return n;
    } else {
      n = n->succ;
    }
  }
  return NULL;
}

nodo *lista_in(nodo *a, int pos, float e) {
  if (pos == 1) {
    a = listain0(a, e);
    return a;
  }
  nodo *r = lista_cerca(a, pos);

  if (r != NULL) {
    nodo *b = malloc(sizeof(nodo));
    b->info = e;
    r->prec->succ = b;
    b->prec = r->prec;
    r->prec = b;
    b->succ = r;
    return a;
  } else {
    return a;
  }
}
