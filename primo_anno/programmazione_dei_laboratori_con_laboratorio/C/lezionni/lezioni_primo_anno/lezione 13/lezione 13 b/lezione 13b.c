/*implementazione di array mbidimensionali (matrici)
in questo caso lo implementeremo attraverso un array di array,
un array di puntatori ad altri array, 
con dimensione dell'array "principale" il numero di righe, ognuno che punta ad un array
lungho quante sono le colonne ( tutte uguali dimensione)*/
#include<stdio.h>
#include <stdlib.h>
#include<string.h>

// esercizio bonus, implementrare una matrice con array lineare in una matrice con array di array

float **crea_matrice(int, int, float *);
void stampa_matrice(float**, int, int);


void main (int dim, char *args[]){// dalla linea di comando metto le informazioni per creare una matrice
                                  // prima stringa = numero di colonne, gli altri gli elementi della matrice
    float *a = malloc(sizeof(float)*dim-2); //creiamo la matricie lineare ( lineare = array lineare)
    int nc,nr, i;
    float f;
    float **mt;

    if (sscanf(args[1], "%d", &nc)<1){
        printf("stringa di help\n");
        return;
    }

    for (i = 2; i<dim; i++){
        if (sscanf(args[i], "%f", &f)==1){
            a[i-2] = f;
        } else{
            a[i-2] = 0;
        }

    }

    nr = (dim-2)/nc;
    if (((dim-2)%nc)!=0)
        nr++;

    mt= crea_matrice(nr, nc, a);
    stampa_matrice(mt, nr,nc);


}


/*
float **crea_matrice(int nr, int nc, float *a ){
    float **mt = malloc(sizeof(float*)*nr);
    if (mt == NULL){
        return NULL;
    }
    int r, c;
    for (r = 0; r<nr;r++){
        mt[r]=malloc(sizeof(float)*nc);
        if (mt[r] == NULL){
            for (;r>=0;r--){
                free(mt[r]);
            }
            free (mt);
            return NULL;
        }
        //inizializazzione elementi della matrice
        
        for(c=0; c<nc; c++){
            mt[r][c] = r*c+1; // doppia parentesi quadra quando sono array di array ricorda !
        }
    }

    return mt;
    
    
}
*/

void stampa_matrice(float **mt, int nr, int nc){
    int r, c;

    for ( r=0; r<nr; r++) {
        for (c=0; c<nc; c++){
            printf("%4.1f ", mt[r][c]);
        }
        printf("\n");
    } 
}



float **crea_matrice(int nr, int nc, float *a ){
    float **mt = malloc(sizeof(float*)*nr);
    if (mt == NULL){
        return NULL;
    }
    int r, c;
    for (r = 0; r<nr;r++){
        mt[r]=malloc(sizeof(float)*nc);
        if (mt[r] == NULL){
            for (;r>=0;r--){
                free(mt[r]);
            }
            free (mt);
            return NULL;
        }
        
        
        for(c=0; c<nc; c++){ 
            mt[r][c] = a[(nc*r)+c];
        }
    }
    return mt;
}
