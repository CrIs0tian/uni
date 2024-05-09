#include <stdio.h>
#include <stdlib.h>
struct punto {
  int x;
  int y;
};
typedef struct punto punto;
void stampa_punto(punto);

int main() {}

void stampa_punto(punto p) { printf("(%d,%d)", p.x, p.y); }
