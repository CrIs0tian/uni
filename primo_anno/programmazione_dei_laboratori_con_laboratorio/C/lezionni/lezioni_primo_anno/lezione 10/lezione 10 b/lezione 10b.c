#include <stdio.h>
// implementazione di scan, scanf e &

// domanda,
// 1)se vogliamo cambiare il valore di una variabile del main
// con una funzione senza che questa diventa una variabile locale,
// come fare?
// 2) se vogliamo convertire un valore da un tipo ad un altro invece?

void incrementa_int(int *);

/*
void main (){
    int x = 10;
    incrementa_int(x);  a meno che noi assegniamo a x il valore di questa
funzione (con return x), così non cambia nulla, come fare? printf("%d\n", x);
}

void incrementa_int(int z){
    z++;
}
*/

// ma se invece del valore, nel parametro metto il puntatore della variabile ?

void main() {
  int x = 10;
  int n, d;
  float f;
  incrementa_int(&x); // uso questa & che ritorna l'indirizzo ( puntatore) della
                      // variabile a destra
  printf("%d\n", x);
  char s[256] = "(123;456.7)"; // posso usare una stringa come input mettendola
                               // prima del parametro di input

  d = scanf("(%d;%f)", &n, &f); // se scritta cosi l'input deve precisamente
                                // rispettare il formato tra virgolette
  printf("%d, %f, %d\n", n, f,
         d);                    /*scanf,  una funzione che quando eseguita,
                  interrompe l'esecuzione del programma e aspetta un input ( input( ) di python
                   praicamente),                    ma scanf può attuare un parcing, ossia convertire in qualcosa
                  (dalle formattazzioni che scegliamo noi) la stringa che scriviamo
                  se va a buon fine(perchè senno ritorna il valore della variabile precedente),
                  verrà salvato nel secondo parametro (che è un PUNTATORE) che mettiamo*/
  sscanf(d, "(%d;%f)", &n, &f); // questa prende come input però una stringa
                                // messa come primo parametro
}

void incrementa_int(int *z) { // ovviamente dobbiamo considerarlo non come un
                              // int ma come un puntatore ad un intero
  (*z)++;
}
