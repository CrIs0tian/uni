#include <stdio.h>
#include <stdlib.h>

/*intorduzione e studio delle union: cosa sono ?
  servono per definire nuovi tipi di dati (come fa le struct)
  una variabile di tipo union può contenere valori di tipo intercambiabile 
  (cioè posso cambiare il tipo di variabile), per quanto riguarda la dimensione 
  è grande quanto la dimensione massima della variabile tra quelle che usiamo  
*/

/*come si inizializza, come se fosse una struct, e avrà la dimensione la grandeza della variabile
  più grande */
void main (int dim, char *args[]){
    union {
        char c_val; // primo valore = campo (come struct) NB: questa inizializzazione si fa dentro il main e si ppuò applicare anche alle struct
        int i_val;
        float f_val;
    } u ;
    u.i_val = 8;
    printf("%d\n", u.i_val);
    u.c_val = 'a';
    printf("%c\n", u.c_val);
    printf("%d\n", u.i_val);// cambaindo valore con campo, la variabile cambia, (da 8 ora stampa 97, la codifica ascii di 'a')
    


}

