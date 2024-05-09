#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct node{
    char *v; 
    struct node *next; 
};
typedef struct node node;
struct linked_list{
    node *a; 
    int n;
}; 
typedef struct linked_list linked_list; 
linked_list move_to_tail(linked_list);
node *search(linked_list, int);
linked_list init(void);
void print_llist(linked_list);
linked_list in0(linked_list , char*);
linked_list insert(linked_list, int, char*);

void main (){
    int e;
    linked_list L = init();
    L = insert(L, 0 ,  "programmazione");
    L = insert(L, 1 ,  "dei");
    L = insert(L, 2 ,  "calcolatori");
    L = insert(L, L.n-1 ,  "pyhton e c");

    print_llist(L);
    printf("------------------------------------------------------\n");

    L = move_to_tail(L);

    print_llist(L);

}

linked_list init(void){
    linked_list L = {NULL, 0};
    return L;
}


linked_list move_to_tail(linked_list L){
    node *a0, *a1;
    a0 = search(L, L.n-1); 
    a1 = L.a; 
    L.a = a1->next;
    a1->next = NULL;
    a0->next = a1;
    return L;
}

node *search(linked_list l, int pos){
    node *p = l.a; // puntatore p al primo elemento della lista (L.a)
    int c = 0;

    while( p!= NULL && c < pos){
        p = p->next;
        c++;
    }
    return p;
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

