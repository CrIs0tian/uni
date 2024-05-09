#include <stdio.h>
#include <stdlib.h>
struct array_int 
{       
    int *a;
    int n;
    int c; // capacità array 

};
typedef struct array_int array_int; 
array_int array_int_init(void);
array_int array_int_append( array_int , int); 
array_int array_int_insert(array_int, int, int );
array_int array_int_pop(array_int);
void array_int_print(array_int);
array_int array_int_delete(array_int a, int i);

void main(){
    
    array_int v = array_int_init(); 
    int i, n=14;                
    for (i=0; i<n; i++){
        v = array_int_append(v, i); //costo medio o(n)/n, costo di ogni singolo append---> COSTO AMMORTIZZATO
        printf("n = %d; c = %d\n",v.n, v.c );
    }
        
    array_int_print(v); //costo o(v.n)
    
    v = array_int_insert(v, v.n, 100);
    
    array_int_print(v); 

    v = array_int_delete(v,4);
    array_int_print(v);
}
    


array_int array_int_init(void){ 
    array_int v = {NULL, 0, 0};
    return v; 
}
array_int array_int_append( array_int v, int e ){
	int i;
	
	if (  v.n == v.c ){
		v.a = realloc(v.a,(2*v.c+1)*sizeof(int));
		v.c = 2*v.c+1;
        
	}
	v.a[v.n] = e;
	v.n++;

    return v;
    /*
    *complessità temporale è o(1) nel caso medio (n append consecutive costano o(n))
    *complessità spaziale o(n) nel caso peggiore perchè viene usata metà della memoria allocata
    */
}
void array_int_print(array_int v){
    int i;

    printf("[");
    for (i = 0; i<v.n; i++){
        printf("%d,", v.a[i]);
    }
    printf("]\n");
} 
array_int array_int_insert( array_int v, int pos, int e){ 
    int old_c = v.c, old_n=v.n;
    if (pos<v.n); 
        return v; 
    v = array_int_append(v,0);

    if (old_c == old_n && old_c==v.c){
        return v; 
    } 
    for (int i = v.n-2; i>=pos; i--){ 
        v.a[i+1]=v.a[i];
    }
    v.a[pos]=e; // insert 

    return v;
}
array_int array_int_pop(array_int v){
    if (v.n > 0){
        v.n--;
        if (v.n<v.c/4){
            v.a = realloc(v.a, (v.c/2+1)*sizeof(int));
            v.c = v.c/2+1; 
        }
    return v; 
    }
}
array_int array_int_delete( array_int v, int i){
    v.a[i]=0;
    for (;i<v.n; i++){
        v.a[i]=v.a[i+1];
    }
    v = array_int_pop(v);
    return v; 
}