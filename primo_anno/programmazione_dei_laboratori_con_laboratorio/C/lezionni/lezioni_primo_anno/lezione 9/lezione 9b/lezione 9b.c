#include<stdio.h>
#include <stdlib.h>
#include <string.h>

/*implmentazione di lsite concatenate di python in C,
  stavolta invece di usare float come elementi usiamo le stringhe
*/  
struct node{
    char *v;  // invece di un float, usiamo una stringa, cioè un puntatore a char
    struct node *next;
};

typedef struct node node; 

struct linked_list{
    node *a; 
    int n;
};

typedef struct linked_list linked_list;
void print_llist(linked_list);
linked_list in0(linked_list, char*);
linked_list init(void);
node *search(linked_list, int);
linked_list del0(linked_list); 
linked_list delete( linked_list, int);
linked_list insert(linked_list, int, char*);
void main (int dim, char *args[]){
    linked_list L = init();
    int i; 

    L = insert(L, 0 ,  "programmazione");
    L = insert(L, 1 ,  "dei");
    L = insert(L, 2 ,  "calcolatori");
    L = insert(L, L.n-1 ,  "pyhton e c");
    L = delete(L, 1);

    print_llist( L); 

    for (i=0; i< dim; i++){
        printf("%s\n", args[i]);
    }

}





void print_llist(linked_list L){
    node *p = L.a;
    while (p != NULL){
        printf("\"%s\"\n", (*p).v); //   \"  nel print stampa le virgolette
        p = p->next;
    }
}






linked_list in0(linked_list L, char *e){
    node *p = malloc(sizeof(node));
    p->v = malloc(sizeof(char)*strlen(e)+1); 
    p->v = strcpy(p->v, e);

    p->next = L.a;
    L.a=p;
    L.n++; 
    return L;
}




linked_list init(void){
    linked_list L = {NULL, 0};
    return L;
}





node *search(linked_list l, int pos){
    node *p = l.a; 
    int c = 0;

    while( p!= NULL && c < pos){
        p = p->next;
        c++;
    }
    return p;
}








linked_list insert(linked_list L, int pos, char *e){
    node *a, *p1;
    if (pos > 0 && pos<=L.n){
        a=malloc(sizeof(node));
        a->v = malloc(sizeof(char)*strlen(e)+1); 
        a->v = strcpy(a->v, e);
        p1=search(L, pos-1);
        a->next = p1->next;
        p1->next = a;
        L.n++;
    } else if (pos == 0){
        L = in0(L,e);
    }
    
    return L;
}







linked_list del0(linked_list L){
    node *p; 
    if (L.n > 0){
        p= L.a;
        L.a = p->next;
        free(p);
        L.n--;
    }
    return L;
}






linked_list delete(linked_list L, int pos){
    node *p1, *p2;
    if (pos > 0 && pos < L.n){
        p1=search(L, pos-1);
        p2= p1->next;
        p1->next = p2->next;
        free (p2->v);
        free(p2);
        L.n--;
    } else if ( pos == 0){
        L = del0( L);
    }

    return L;

}
