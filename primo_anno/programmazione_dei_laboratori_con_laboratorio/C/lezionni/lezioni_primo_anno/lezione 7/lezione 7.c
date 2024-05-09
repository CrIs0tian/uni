#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
 *operazioni per implementare le liste su c 
 (esempio lista = {1, 2, tre, latte, 8.76})
 ARRAY A DIMENSIONE VARIABILE
*/ 

/*
    creazione di una struct, che contiene due informazioni, 
    un puntatore a void  e un char per etichettare il tipo di dati
    considerati da ogni singolo puntatore (che sono elementi dell'array di puntatori)

*/

struct object {
    char type; // 'i', 'c', ed 's' per int, char, e stringa
    void *pointer; 
};
typedef struct object object; 

void set(object*,int,object);

void main ( ){
    object L[10];  // array di 10 object
    char a[]="programmazione";
    int i; 

    L[0].pointer =malloc(sizeof(int)); // output = indirizzo ad una sezione di memoria dedicata alla sezioen 0 dell'object per metterci un int 
    L[0].type = 'i'; // indico il tipo di puntatore ( in questo caso ad int)
    *( (int*)(L[0].pointer)) = 3; // ((int*= casting, assegno momentaneamente a quell'indirizzo il tipo di dato a cui sta puntando, sennò farebbe errore))

    L[1].pointer= malloc(sizeof(char));
    L[1].type= 'c';
    *((char*)(L[1].pointer))='x';// con *(puntatore) = valore assegno un valore alla cella di memoria a cui il puntatore sta puntando 

    L[2].pointer = (void*)a; // assegna un altro puntatore ad un dato già allocato ( il char a in questo caso)
    L[2].type = 's';
    
    printf("[");
    
    for(i = 0; i<3; i++){
        if ( L[i].type == 'i')
            printf( "%d, ", (*(int*)(L[i].pointer)));
        else if (L[i].type == 'c')
            printf("%c, ",( *(char*)(L[i].pointer)));
        else printf( "%s,",(char*)(L[i].pointer));// cosi chiamo la stringa, se lo avessi scritto come quelli sopra avrei stampato il primo char
    }

    printf("]\n");
}

/*creiamo una funzione che faccia quello che abbiamo fatto adesso, 
  assegnazione ad un puntatore un valore ed il suo tipo e le operazioni 
  di stampa etc. 
*/
void set( object *L,int p, object e ){
    L[p].type = e.type;
    if (L[p].type == 'i'){
        L[p].pointer = malloc(sizeof(int));
        *((int*)(L[p].pointer)) = (*(int*)e.pointer);     
    } else if (L[p].type == 'c'){
        L[p].pointer = malloc( sizeof(char));
        *((char*)(L[p].pointer)) = *((char*)e.pointer);
    }
    else {
        L[p].pointer = malloc( sizeof(char)*(strlen((char*)e.pointer)+1)); //strlen restituisce la lunghezza di una stringa, escluso '\0'
        strcpy(e.pointer, L[p].pointer); // copia di una stringa (mettendo come paramtero il suo puntatore)e e la stampa ad un altra ( la seconda)

    }
}