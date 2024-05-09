#include<stdio.h>
#include<stdlib.h>
void main( int dim, char *args[]){
    int i;
    float somma=0;
    for (i=0; i<dim; i++){
        float s=0;
        sscanf(args[i],"%f", &s);
        somma+=s;
    }
    printf("somma = %3.3f\n", somma);
    int n=sizeof(char*);
    int b = sizeof(int*);
    printf("%d  %d", n, b);
    
}