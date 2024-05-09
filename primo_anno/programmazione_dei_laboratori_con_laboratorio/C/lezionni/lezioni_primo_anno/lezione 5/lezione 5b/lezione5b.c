#include<stdio.h>
#include<stdlib.h>
// introduzione struct , contenitore di diversi tipi dati, e typedef, crea un nuovo nome per un tipo gia esistente
struct array_int //nome del tipo di struct 
{       //dati all'interno = campi
    int *a;
    int n;

};
typedef struct array_int array_int; // sintassi typedef / nome vecchio del tipo / nuovo nome di tipo
// si usa come un tipo di dato qualsiasi
array_int array_int_init(void);
array_int append_array( array_int v, int e);

void main(){
    array_int v = array_int_init(); //v diventa uno struct di tipo array_int come specificato sopra
    int i;                          //con 2 campi
    v.a = malloc(10*sizeof(int));//variabile.campo ---->viene specificato il campo nello struct che si vuole usare
    v.n=10;

    for (i=0;i<v.n;i++){
        v.a[i]= i*12;

    }
    for (i=0;i<v.n;i++){
        printf("%d\n",v.a[i]);
         
    }

}

array_int array_int_init(void){//void non da niente come parametro
    array_int v= {NULL, 0};// assegno in ordine ad ogni campo un valore
    return v; //ritorna un puntatore 'copia dell'array creato nella funzione main
}
array_int append_array( array_int v, int e){
	int i;
	int *a = malloc(v.n*sizeof(int)); // errore, ricorda di moltiplicare per sizeof(int)
	
	if ( a != NULL) { // malloc e' andata a buon fine
		for(i = 0; i < v.n; i++){
			a[i] = v.a[i]; // ORRORE :-) significa a[i] = x[i]
		}
		a[v.n] = e;
	}
	v.n++;
    free(v.a); //NB non viene cancellato ma deallocato cioè tolto il puntatore e viene lasciato lì nella memoria che verrà poi sovrascritta
    v.a=a;
	return v;
}
//altro modo di implementare l'append con lo struct

