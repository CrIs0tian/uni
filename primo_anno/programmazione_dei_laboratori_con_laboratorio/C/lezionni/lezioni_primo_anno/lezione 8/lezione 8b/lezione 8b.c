#include <stdio.h>
#include<stdlib.h>
#include<string.h>
/*inplementazione di liste concatenate di python in c
  cosa sono le liste concatenate? liste che non sono come gli array, ogni
  elemento è in allocazioni di memoria distanti e non continue,
  PRO---> ottimizzazione di occupazione spazi di memoria 
  CONTRO----> maggiore difficolta (+costo) nella indicizazzione/ricerca(dato che non sono array)
*/
struct node {
    float v; // informazione dell'i-esimo elemento della lista concatenata
    struct node *next; // puntatore alla struct node successiva
};

typedef struct node node;

struct linked_list{
    node *a;//puntatore al primo elemento della sequenza
    int n;//size della lista
};
typedef struct linked_list linked_list;
void print_llist(linked_list);
// funzione che mette un elemento nella posizione 0 della lista
linked_list in0(linked_list, float);// output , la lista modificata
linked_list init(void);
node *search(linked_list , int );
void main(){
  linked_list L = init();
  int e;

  for (e = 0; e< 10; e++){
    L=in0(L, (e+1)*11.1);
  }

  print_llist(L);

}


void print_llist(linked_list L){
  node *p = L.a;
  while (p != NULL){
    printf("%f\n", (*p).v);
    // p = (*p).next; possiamo ma si può usare un altro metodo, se p è un PUNTATORE AD UN ALTRA STRUTTURA
    p = p->next;// se p punta ad una struttura puoi accedere direttamente al suo campo cosi 

  }
  
}
linked_list in0(linked_list L, float e){
  node *p = malloc(sizeof(node));
  p->v = e;
  p->next = L.a;
  L.a=p;
  L.n++;
  return L;
}

linked_list init(void) {
	linked_list L = {NULL, 0};
	return L;
}

node *search(linked_list L, int pos){
  /*
  restituisce il puntatore al node in posizione pos di L.
  NULL se la posizione pos non esiste
  
  */
}// continuo nel file successivo 