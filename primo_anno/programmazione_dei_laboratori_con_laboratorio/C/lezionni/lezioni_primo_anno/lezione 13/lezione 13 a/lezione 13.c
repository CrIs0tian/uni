/*introduzione matrice, cioè array multidimensionali 
 in questo caso implementiamo una semplice array lineare con parametri particolari
 il numero di rige (r) e il numero di colonne (c)
*/
#include <stdio.h> 
#include <stdlib.h>
#include <string.h> 
/*creiamo una funzione che crea una matrice quadrate 
che contiene nella posizione [i,j] = i*j*/
float *crea_matrice(int, int);
void stampa_matrice( float*, int, int);
void stampa_posizione(float *, int, int);

void main (){
    float *m = crea_matrice(4,7);

    stampa_matrice(m, 4, 7);

    stampa_posizione ( m, 7, 9);
}

float *crea_matrice(int nr, int nc){
    float *mt = malloc(sizeof(float)*nr*nc);
    int r, c;
    if (mt == NULL){
        return NULL;
    }
    for (r=0; r<nr;r++){
        for(c=0; c<nc;c++){
            mt[nc*r+c] = r*c+1;
        }
    }
    return mt;
}

void stampa_matrice(float *mt, int nr, int nc){
        int r, c;
        for (r=0; r<nr;r++){
            for(c=0; c<nc;c++){
                printf("%4.1f ", mt[nc*r+c]); // il 2 nel %d per dare un massimo di spazi massimi, mentre \t fa la tabulazione
        }
        printf("\n");
    }
}

/*
    mt è una matrice di nc colonne memorizzata per righe
    p è un indice in mt

    stampa l'elemento in posizione p di mt e ne stampa le coordinate (riga, colonna)
*/

void stampa_posizione( float *mt, int nc, int p){
    int c, r;
    c = p %nc;
    r = p/nc; // ricorda qua il / fa la divisione fra interi 

    printf("M[%d, %d] = %2.1f", r, c, mt[p]);

}

