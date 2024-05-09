#include <stdio.h>
#include <stdlib.h>
// introduzione in c del concettto di stringa come array di char
char *str_cat(char *, char *);
int len_str(char *);
int lung(char *, int);
void main() {
  char a[] = "programmazione";
  char b[] = "la madonna";
  // alla fine di questa sequenza nella compilazione verrà creato un array
  // di lunghezza n+1 (l'ultimo in più è un carattere speciale per capire quando
  // la stringa è finita-----> '\0')
  printf("dio mio \"%s\"\n",
         a); // comando per stamparlo usando il pedice s--> (stringa), (\" se
             // voglio stampare anche le virgolette)
  char *c;
  c = str_cat(a, b);
  printf("%s", c);
}

char *str_cat(char *a, char *b) { // funzione già ottimizzata
  char *
      c; // lungezza= len(a) + len(b) + 1, e dovrò calcolarla con un funzione a
         // parte se faccio siezof(a) dentro la funzione uscira SEMPRE 8 RICORDA
  int l = len_str(a),
      n = len_str(b); // costi O(n) e O(m)---->(n,m lunghezze dei due array)
  c = malloc((l + n + 1) * sizeof(int)); // ricorda, crea un indirizzo!
  int i;
  for (i = 0; i < l; i++) { // costo O(n)
    c[i] = a[i];
  }
  for (; i < n; i++) { // puoi anche scrivere cosi senza dover mettere la
                       // condizione iniziale,
                       // basta che la variabile sia già inizializzata
    c[i] = b[i - l];   // costo O(m)
  }
  c[i] = '\0';
  return c;
}

int len_str(char *a) {
  int n = 0;
  while (a[n] != '\0') {
    n++;
  }
  return n;
}
