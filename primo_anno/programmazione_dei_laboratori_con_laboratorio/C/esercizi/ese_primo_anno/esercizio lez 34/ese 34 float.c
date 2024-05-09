#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct node{
    float v; 
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
linked_list in0(linked_list , float );

void main (){
    int e;
    linked_list L = init();
    for (e=0; e<10; e++) {
        L=in0(L, (e+1)*11.1);
    }

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
        printf("%f\n", (*p).v);
        p = p->next;
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