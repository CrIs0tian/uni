#include <stdio.h>
// N.B -variabile = nome riservato ad un pezzo di memoria di taglia rispetto al
// tipo di variabile
//     -non esiste il tipo di variabile stringa
int main() {
  int n = 10;
  int m;
  float x = 3.14;
  double y = x; // float con doppia precisione	, occupa il doppio dei byte
                // rispetto ad un float
  float w = 0, z;
  char c = 'a'; // con l'apice singolo non indico una stringa, ma un singolo
                // carattere
  printf("%f", y);
  printf("%f", y);
}
