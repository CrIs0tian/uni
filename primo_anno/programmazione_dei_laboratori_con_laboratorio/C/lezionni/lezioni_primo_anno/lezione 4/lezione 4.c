#include <stdio.h>
#include <stdlib.h>
// quando viene eseguita una funzione, il tutto avviene all'interno della memoria locale usata per la funzione
// e quando la funzione finisce il suo lavaro, tutte le variabili al suo interno vengono riallocate  
// cosa fare per evitare? si usano funzioni incluse in una libreria specifica (stdlib.h) e il tipo di dato puntatore

void change_array(int x[], int n);
int *copy_array( int *x, int n );
int *append_array( int *x, int n, int e );

void main(){
	int d[15] = {0, 10, 20, 30, 40};
	int i, len_d = sizeof(d)/sizeof(int);
	int *p; // questo è un puntatore in p (implicitamente viene specificata la taglia/dimensione)
	int b[10] = {1,2};
	int len_b = sizeof(b)/sizeof(int);
	int len_p;
	
	
	change_array(d, len_d);
	for(i = 0; i < len_d; i++){
		printf("%d, ", d[i]);
	}
	printf("\n");
	
	p = copy_array(d, len_d);
	len_p = len_d;
	if (p != NULL) {
		for(i = 0; i < len_d; i++){
			printf("%d, ", p[i]);
		}
		printf("\n");
	} else {
		printf("Errore di memoria\n");
	}
	p = append_array(p, len_p, 100);
	len_p++;
	if (p != NULL) {
		for(i = 0; i < len_p; i++){
			printf("%d, ", p[i]);
		}
		printf("\n");
	} else {
		printf("Errore di memoria\n");
	}
}

int *append_array( int *x, int n, int e ){
	int i;
	int *a = malloc((n+1)*sizeof(int));
	
	if ( a != NULL) { // malloc e' andata a buon fine
		for(i = 0; i < n; i++){
			a[i] = x[i]; // ORRORE :-) significa a[i] = x[i]
		}
		a[n] = e;
	}
	free(x); //prende in input un puntatore utilizzato e dealloca la memoria puntata da p
	         // di fatto 'pulendo' quello spazio di memoria
	return a;
}

int *copy_array( int *x, int n ){ // equivalente a (int x[], int n)
	int i;
	int *a = malloc(n*sizeof(int)); // funzione malloc (presente in libreria stdlib.h) == ritorna un indirizzo del primo byte dello spazio di allocazione di dimensione x (quella specificata tra parentesi)
	//allocata nella memoria locale
	
	if ( a != NULL) { // malloc e' andata a buon fine
		for(i = 0; i < n; i++){
			(a+i)[0] = x[i]; // ORRORE :-) significa a[i] = x[i]
		}  //  posizione dell'intero successivo nell'array, non del byte successivo 
	
	return a;
	}
}


void change_array(int x[], int n){
	int i;
	for (i = 0; i < n; i++){
		x[i] = 10*i;
	}
}