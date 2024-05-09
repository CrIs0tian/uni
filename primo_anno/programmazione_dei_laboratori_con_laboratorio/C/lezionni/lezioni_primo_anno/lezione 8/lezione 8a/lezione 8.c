/*
finalizazzione delle implementazioni delle liste
creazioni di funzioni per implementare l'indicizazzione delle liste
*/
#include<stdlib.h>
#include<stdio.h>
#include <string.h>
struct object{
    char type;
    void *pointer;
     // 'i', 'c' ed 's' per int, char e stringa
};
typedef struct object object; 
struct list{
    object *a; // array di object
    int n; // dimensione di a
};
typedef struct list list;
// tre funzioni object che ritornano un int, un char e una stringa,
// quindi possiamo assegnare un valore senza fare i macelli di prima
object new_int(int);
object new_char(char);
object new_string_alias(char*);
object new_string_clone(char*);
void print_list(list);
//  ^ serve per stampare una lista

void main (){
    list L = {NULL, 10};
    L.a=malloc(sizeof(object)*L.n);
    char a[]="programmazione";
    int i;

    L.a[0] = new_int(4); 
    L.a[1] = new_char('a');
    L.a[2]= new_string_alias(a);
    L.a[3]= new_string_clone("questa non è una lista python");
    L.a[9]=new_int(4);
    
    a[0]='h';
    print_list(L);

}

void print_list(list L){
    printf("[");
    int i;

    for(i=0; i<L.n; i++){
        if (L.a[i].type == 'i'){
            printf( "%d ,", *((int*)L.a[i].pointer));
        }
        else if (L.a[i].type == 'c'){
            printf( "%c ,", *((char*)L.a[i].pointer));
        }
        if (L.a[i].type == 's'){
            printf( "%s ,", (char*)L.a[i].pointer);
        }
    }
    printf("]\n");


}

object new_int(int v){
    object ob={'i', NULL};
    ob.pointer = malloc(sizeof(int));
    *((int*)(ob.pointer))=v;
    return ob;
}
object new_char(char a){
    object ob={'c', NULL};
    ob.pointer = malloc(sizeof(char));
    *((char*)(ob.pointer))=a;
    return ob;
}
object new_string_alias(char *p){  /*due modi per le stringe, o crei un alias, quindi stessa allocazione, o crei una copia*/
    object ob={'s', NULL};
    ob.pointer = p; // ob.pointer è un alias, complessità temporale e spaziale O(1)
    return ob;
}

object new_string_clone(char *p){   // ob.pointer è una copia, ma è meno efficiente, complessità temporale e spaziale O(strlen(v))
    object ob={'s', NULL};
    ob.pointer=malloc(sizeof(char*)*strlen(p)+1);
    ob.pointer = strcpy(ob.pointer,p);
    return ob;
}

/*ecco perchè in python la funzione len ha costo O(1)mentre strlen ha costo O(n)
perchè in len lui controlla solo un campo, L.n

*/
