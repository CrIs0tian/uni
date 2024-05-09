/*creazione di strutture (struct) dinamiche
 *per simulare le liste di python
 */

#include <stdio.h>
#include <stdlib.h>
struct array_int 
{                      
    int *a;
    int n;
};
typedef struct array_int array_int; 
array_int array_int_init(void);
array_int array_int_append( array_int , int); 
void array_int_print(array_int);

void main(){
    array_int v = array_int_init(); 
    int i, n=14;                
    for (i=0; i<n; i++){
        v = array_int_append(v, i*10); //costo o(n^2)
    }
        
    array_int_print(v); //costo o(v.n)
}

array_int array_int_init(void){ //o(1)
    array_int v = {NULL, 0};
    return v; 
}
array_int array_int_append( array_int v , int e){
	int i;
	int *a = malloc((v.n+1)*sizeof(int)); // costo spaziale(n) memoria aggiuntiva
	
	if ( a != NULL) { 
		for(i = 0; i < v.n; i++){   
			a[i] = v.a[i];  
		}
		a[v.n] = e;   
	    v.n++;   
        free(v.a);  
        v.a=a;  
	return v; 
    }
}
void array_int_print(array_int v){
    int i;

    printf("[");
    for (i = 0; i<v.n; i++){
        printf("%d,", v.a[i]);
    }
    printf("]\n");
}
