#include <stdlib.h>
#include <stdio.h>
struct array_int
{
    int *a;
    int n; 
    int c;
};
typedef struct array_int array_int;
array_int array_int_init(void);
array_int array_int_append(array_int, int);
array_int trova_spazi(char *);
void array_int_print(array_int);


void main(){
    char a[] ="          ";
    array_int v = trova_spazi(a);
    array_int_print(v);

}

array_int array_int_init(void){
    array_int v={NULL, 0,0};
    return v;
}

void array_int_print(array_int v){
    int i;

    printf("[");
    for (i=0; i<v.n;i++){
        printf("%d, ",v.a[i]);
    }
    printf("]\n");
}
array_int array_int_append(array_int v, int e){
    int i;
    int *a;
    
    if (v.n==v.c){
        a=malloc((2*v.c+1)*sizeof(int)); 
        if (a==NULL){
            return v;
        }
        for (i=0; i<v.n;i++){
            a[i]=v.a[i];
        }
        v.c=2*v.c+1;
        free(v.a);
        v.a=a;
    }
    v.a[v.n]=e;
    v.n++;
    
    return v;
}
array_int trova_spazi(char *a){
    array_int v = array_int_init();
    int i=0;
    while (a[i] != '\0'){
        if (a[i] ==' '){
            v=array_int_append(v, i);
        }
        i++;
    }
    return v;
}