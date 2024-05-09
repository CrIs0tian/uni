/*implementazione dei dizionari in C, 
operazini di update, ricerca con parole
chiave e eliminazione*/  

//minuto 17/09

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct dict_item{
    char *k; // chiave = stringa
    float v;// valore = float
};
typedef struct dict_item dict_item;
struct node{
    dict_item info; //nodo che contiene le info ( chiave, valore) strutturati come linked_list
    struct node *next;
};
typedef struct node node;
struct linked_list{
    node *a;
    int n;
};
typedef struct linked_list linked_list;
struct dict{
    node **a; //un array di node( quindi array di puntatori)
    int n; 
    int M; //capacità array
};
typedef struct dict dict;

dict dict_init(int);
int h(dict, char*);
dict dict_set(dict, dict_item);
node *dict_search(dict, char*);
void print_dict(dict);
int dict_del(dict, char*);
dict dict_resize(dict, int);

void print_llist(node*);
node *in0(node*, dict_item);






void main (int dim, char *args[]){
    dict d = dict_init(3);
	int i;
	dict_item e;
	
	for(i = 1; i < dim; i++){
		e.k = args[i];
		e.v = i;
		d = dict_set(d, e);
	}

    dict_del(d, args[dim-1]);

    print_dict(d);
}
/* funzione hash (h(k))
   ritorna un indice del dizionario, che se ben implementata, garantisce un valore k tale che
   il costo di ricerca di una chiave sia o(n/m) costante ( n = numero chiavi, m= lunghezza array)
   
   una possibile funzione sarebbe quella di prendere una chiave, la divide in byte, 
   facciamo lo xor bit a bit, ed esce un numero h(k), se questo numero è tropo grosso (h(k)>M) facciamo il mod M del numero 
*/

int h(dict d, char *k){

    // operatori logici bit a bit:
    // ^ XOR
    // & AND
    // | OR

    int hash_val = 0, i = 0; // valore che retituiremo nella funzione 
    while (k[i] != '\0'){
        hash_val = hash_val ^ k[i];  // ricorda, k[i]= char (1 byte = 8 bit)
        i++;
    }
    return hash_val % d.M;
}


dict dict_set(dict d, dict_item e){
    int p = h( d, e.k); 
    node *nd;
    nd = dict_search(d, e.k);
    if (nd != NULL){
        nd->info.v = e.v;
    } else {
        d.a[p] = in0(d.a[p], e);
        d.n++;
    }
    if ( d.n/d.M > 4){
        d = dict_resize(d, d.M*2+1);
    }
    return d;
}
/*ritorna il puntatore al node contenente l'item del dizionario con 
 chiave k. NULL se tale chiave non è presente nel dizionario
*/

node *dict_search(dict d, char *k){
	int p = h(d, k);
	node *q = d.a[p];
	
	while( q != NULL && strcmp(k, q->info.k) != 0){
		q = q->next;
	}
	
	return q;
}






void print_dict(dict d){
	int i;
	for (i = 0; i < d.M; i++){
		printf("%d ", i);
		print_llist(d.a[i]);
		printf("\n");
	}
}

dict dict_init(int M){
    dict d; 
    int i; 
    d.a= malloc(sizeof(node*)*M);
    d.n=0; 
    d.M=M;
    for (i=0; i<d.M;i++){
        d.a[i]=NULL;
    }
    return d;

}



/*
funzione per rimuovere un item della chiave k inserita*/
int dict_del(dict d, char* k){
    int p = h(d, k);
    node *nd, *x;  
    nd = dict_search( d, k);
    if (nd == NULL){
        return 0;
    }
    if (d.a[p] == nd){
        d.a[p] = nd->next;
    } else{
        x = d.a[p];
        while (x->next != nd){
            x = x->next;
        }
        x->next = nd->next;
    }
    free(nd);
    d.n--;
    return 1;

}




/***************************************************************************************************/


node *in0(node *nd, dict_item e){
	node *p = malloc(sizeof(node));
	
	p->info = e;
	p->next = nd;
	nd = p;
		
	return nd;
}



void print_llist(node *nd){
	node *p = nd;
	
	while( p != NULL ){
		printf("(\"%s\", %f) ", p->info.k, p->info.v);
		p = p->next; /*equivalente a p = (*p).next */
	}
}

dict dict_resize ( dict d0, int new_M){
    dict d1 = dict_init(new_M);
    int i; 
    node *q;

    for (i= 0; i<d0.M; i++){
        while (d0.a[i] != NULL){
            d1 = dict_set(d1, d0.a[i]->info);
            //cancello ora d0.a[i]
            q= d0.a[i];
            d0.a[i] = q->next;
            free(q);
        }
    }
    free(d0.a);
    return d1;
}







