#include<stdio.h>
#include <stdlib.h>
#include <string.h>
struct object{
    char type;
    void *pointer;
};
typedef struct object object;

struct list{
    object *a;
    int n;
    int c;
};
typedef struct list list;

object new_int(int);
object new_char(char);
object new_string_alias(char*);
object new_string_clone(char*);
void print_list(list);
list list_append(list, object);
list pop_list(object);
void list_init(list);



void main(){
    list L = {NULL, 10, 20};
    L.a=malloc(sizeof(object)*L.c);   
    object b;
    b = new_int(5);
    list_append(L, b);
    print_list(L);
    
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
object new_string_alias(char *p){  
    object ob={'s', NULL};
    ob.pointer = p; 
    return ob;
}

object new_string_clone(char *p){   
    object ob={'s', NULL};
    ob.pointer=malloc(sizeof(char*)*strlen(p)+1);
    ob.pointer = strcpy(ob.pointer,p);
    return ob;
}
list list_append(list l, object b){
    
    if (l.n==l.c){
        l.a = realloc( l.a, (sizeof(object)*l.c)*2+1);
        l.c=l.c*2+1;
    }
    l.a[l.n].type=b.type;
    l.a[l.n].pointer=malloc(sizeof(int));
    *((int*)(l.a[l.n].pointer))=*((int*)(b.pointer));

}
void print_list(list L){
    printf("[");
    int i;

    for(i=0; i<=L.n; i++){
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